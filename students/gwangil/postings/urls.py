from django.urls import path
from .views import PostingView, ImageView, CommentView, LikeView

urlpatterns = [
# http://127.0.0.1:8000/postings
    path('', PostingView.as_view()),
# http://127.0.0.1:8000/postings/images
    path('/images', ImageView.as_view()),
# http://127.0.0.1:8000/postings/comments
    path('/comments', CommentView.as_view()),
# http://127.0.0.1:8000/postings/likes
    path('/likes', LikeView.as_view())
]


