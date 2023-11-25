from django.db import models
from user.models import UserProfile
from post.models import Post

class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    members = models.ManyToManyField(UserProfile, related_name='groups', blank=True)
    posts = models.ManyToManyField(Post, related_name='group_posts', blank=True)
    group_messages = models.ManyToManyField('GroupMessage', related_name='group', blank=True)

    def __str__(self):
        return self.name


class GroupMessage(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message by {self.author} in {self.created_at}'

