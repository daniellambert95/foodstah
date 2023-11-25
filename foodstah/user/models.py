from django.db import models
from django.contrib.auth.models import User
from post.models import Post
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(default="default.jpg", upload_to='profile_pictures/', blank=True, null=True)
    following = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='followed_by')
    followers = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='follows')
    saved_posts = models.ManyToManyField(Post, related_name='saved_by', blank=True)

    def __str__(self):
        return self.user.username

    def get_profile_picture(self):
        if self.profile_picture:
            return self.profile_picture.url
        return settings.MEDIA_URL.get_default()

