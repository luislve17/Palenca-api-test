from django.urls import path, include

from . import views

urlpatterns = [
    path('login', views.LoginAPI.as_view(), name='uber-login'),
    path('get-profile/<str:token>', views.get_profile, name='uber-get-profile'),
]