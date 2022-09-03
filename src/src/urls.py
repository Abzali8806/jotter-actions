from django.contrib import admin
from django.urls import path, include
from forum.views import home_view, create_post_view, blog_view, post_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('forum.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]
