from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('user.UserProfile', on_delete=models.CASCADE)
    description = models.TextField()
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)
    tags = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='post_photos/')
    comments = models.ManyToManyField('Comment', related_name='post_comments', blank=True)
    likes = models.ManyToManyField('user.UserProfile', related_name='liked_posts', blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def clean(self, *args, **kwargs):
        if not self.slug:
            slug_title = slugify(self.title)
            slug_date = slugify(self.date_created)
            self.slug = f"{slug_title}-{slug_date}"
        super().clean(*args, **kwargs)

class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey('user.UserProfile', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
