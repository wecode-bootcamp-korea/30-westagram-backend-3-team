from django.urls import path
from .views import SignUpView, LoginView

# http://127.0.0.1:8000/users/signup
urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/login', LoginView.as_view())
]
