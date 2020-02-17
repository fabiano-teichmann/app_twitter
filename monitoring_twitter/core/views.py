from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import generic

from core.manage_request_twitter import ManagerRequestApiTwitter
from core.models import Tweet, Hashtag


@method_decorator([login_required], name='dispatch')
class TweetView(generic.ListView):
    model = Tweet
    template_name = 'list_tweets.html'

    def get(self, request, *args, **kwargs):
        tweets = self.model.objects.all().order_by('-date_publish')
        return render(request, self.template_name, {'tweets': tweets})


@method_decorator([login_required], name='dispatch')
class CreateHashTagView(generic.CreateView):
    model = Hashtag
    template_name = 'create_hashtag.html'

    def post(self, request, *args, **kwargs):
        pk_user = request.user.pk
        input_hashtag = self.get_input()
        if input_hashtag:
            hashtag_exist = self.model.objects.filter(hashtag=input_hashtag).count()
            if hashtag_exist:
                messages.warning(request, 'Essa hashtag já existe.')
            else:
                hashtag = self.model.objects.create(hashtag=input_hashtag, user_id=pk_user)
                self.get_tweets(hashtag)
        return redirect('/list_hashtags')

    def get_tweets(self, hashtag):
        total_tweets = ManagerRequestApiTwitter().update_tweets(hashtag)
        if total_tweets:
            msg = f"Hashtag criada com sucesso foi encontrado {total_tweets} com a hashtag {hashtag.hashtag}"
            messages.info(self.request, msg)
        else:
            msg = 'Não Houve um problema inesperado'
            messages.warning(self.request, msg)

    def get_input(self):
        input_hashtag = self.request.POST['hashtag']
        if input_hashtag:
            if '#' not in input_hashtag:
                input_hashtag = '#' + input_hashtag
            return input_hashtag
        else:
            messages.warning(self.request, 'Não foi digitado nenhuma hashtag')
        return None


@method_decorator([login_required], name='dispatch')
class DeleteHashTagsView(generic.DeleteView):
    model = Hashtag
    success_url = '/list_hashtags'


@method_decorator([login_required], name='dispatch')
class ListHashtagsView(generic.ListView):
    model = Hashtag

    def get(self, request):
        hashtags = Hashtag.objects.all()
        return render(request, 'list_hashtags.html', {'data': hashtags})


@login_required()
def delete_hashtag(request, pk):
    if request.method == 'GET':
        Hashtag.objects.filter(pk=pk).delete()
        return redirect('/list_hashtags')


def update_hashtag(request):
    if request.is_ajax():
        list_hashtag_updated = ManagerRequestApiTwitter().get_hashtags_for_update()
        return JsonResponse({'total_hashtags_updated': len(list_hashtag_updated), 'status': 'success'})
    else:
        return JsonResponse({'status': 'fail'})