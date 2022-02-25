from django.urls import path

from postings.views import PostingView, CommentView, LikeView, ImageView

urlpatterns = [
    path('/posting', PostingView.as_view()),
    path('/image', ImageView.as_view()),
    path('/comment', CommentView.as_view()),
    path('/like', LikeView.as_view())
]