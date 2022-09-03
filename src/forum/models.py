from django.utils.text import slugify
from datetime import datetime
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, default=1, null=True,
    on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)
    category = models.CharField(max_length=255)
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = "post-" + slugify(self.title)
        super().save(*args, **kwargs)