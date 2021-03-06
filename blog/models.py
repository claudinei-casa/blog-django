from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Created On')
    last_modified = models.DateTimeField(auto_now=True)

    # to order posts blog

    class Meta:
        ordering = ['-created_on']  # ('-created_on',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})
