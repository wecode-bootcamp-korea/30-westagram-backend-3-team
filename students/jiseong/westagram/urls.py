from django.urls import path, include

urlpatterns = [
    path('signup/', include('users.urls')),
]