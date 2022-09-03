from django.urls import path
from .views import login_view, register_view, profile_view

urlpatterns = [
    path('login_user/', login_view, name='login'),
    path('sign_up/', register_view, name='sign_up'),
    path('profile/', profile_view, name='user_profile')
]
