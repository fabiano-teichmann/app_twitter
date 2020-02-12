from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import generic

from core.forms import HashtagForm
from core.models import Tweet, Hashtag


@method_decorator([login_required], name='dispatch')
class TweetView(generic.ListView):
    model = Tweet
    template_name = 'list_tweets.html'


@method_decorator([login_required], name='dispatch')
class CreateHashTagView(generic.CreateView):
    model = Hashtag
    template_name = 'create_hashtag.html'

    def post(self, request, *args, **kwargs):
        pk_user = request.user.pk
        hashtag = request.POST['hashtag']
        if hashtag:
            if '#' not in hashtag:
                hashtag = '#' + hashtag
            hashtag_exist = self.model.objects.filter(hashtag=hashtag).count()
            if hashtag_exist:
                messages.warning(request, 'Essa hashtag já existe.')
                return redirect('/list_hashtags')
            self.model.objects.create(hashtag=hashtag, user_id=pk_user)
            return redirect('/list_hashtags')


@method_decorator([login_required], name='dispatch')
class DeleteHashTagsView(generic.DeleteView):
    model = Hashtag
    success_url = '/list_hashtags'


@method_decorator([login_required], name='dispatch')
class ListHashtagsView(generic.ListView):
    model = Hashtag

    def get(self, request):
        user_id = request.user.pk
        # hashtags = self.model.objects.filter(user_id=user_id)
        hashtags = Hashtag.objects.all()
        # return HttpResponse(hashtags)
        return render(request, 'list_hashtags.html', {'data': hashtags})


@login_required()
def delete_hashtag(request, pk):
    if request.method == 'GET':
        Hashtag.objects.filter(pk=pk).delete()
        return redirect('/list_hashtags')