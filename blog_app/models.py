from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=200)
  post_desc = models.TextField()
  image = models.ImageField(default="defaultpost.jpg", upload_to='post_pics')
  created_on = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
    return self.title
  

class Comment(models.Model):
  posted_by = models.CharField(max_length=100, blank=False)
  commenter_email = models.EmailField(blank=False)
  commenter_website = models.CharField(max_length=100, blank=False)
  comment_desc = models.CharField(max_length=300, blank=False)
  commenter_image = models.ImageField(default="default.jpg", upload_to='profile_pics')
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  created_on = models.DateTimeField(default=datetime.now, blank=True)
  
  def __str__(self):
    return self.posted_by
  

class Reply(models.Model):
  comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='reply')
  replied_by = models.CharField(max_length=100)
  reply_desc = models.CharField(max_length=300)
  created_on = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
      return self.replied_by
  