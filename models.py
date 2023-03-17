from email.policy import default
from enum import auto
from io import open_code
from pickle import TRUE
from sqlite3 import Timestamp
from turtle import mode
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post,related_name = "comments",on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    data_added  = models.DateTimeField(auto_now_add = TRUE)   

    def __str__(self):
        return '%s - %s' %(self.post.title,self.user)
