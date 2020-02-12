from django.urls import path

from core import views

urlpatterns = [
    path('', views.TweetView.as_view(), name='tweet'),
    path('create_hashtag', views.CreateHashTagView.as_view(), name='create_hashtag'),
    path('list_hashtags', views.ListHashtagsView.as_view(), name='list_hashtags'),
    path('delete_hashtag/<pk>', views.delete_hashtag, name='delete_hashtag')

]
