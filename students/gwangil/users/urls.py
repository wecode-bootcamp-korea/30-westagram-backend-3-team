from django.urls import path
from .views import UserView

# http://127.0.0.1:8000/users/
urlpatterns = [
    path('', UserView.as_view())
]
