from django.urls import path
from .views import SignUpView, LoginView, FollowView

urlpatterns = [
# http://127.0.0.1:8000/users/signup
    path('/signup', SignUpView.as_view()),
# http://127.0.0.1:8000/users/login
    path('/login', LoginView.as_view()),
# http://127.0.0.1:8000/users/follow
    path('/follows', FollowView.as_view())
]
