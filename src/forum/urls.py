from django.urls import path
from .views import home_view, create_post_view, blog_view, post_view

urlpatterns = [
    path('', home_view, name='home'),
    path('create_post/', create_post_view, name='create_post'),
    path('blog/', blog_view, name='blog'),
    path('<slug:slug>', post_view, name='post'),
]
