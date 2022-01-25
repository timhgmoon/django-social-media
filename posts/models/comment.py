from django.db import models
from django.contrib.auth import get_user_model
from .post import Post

#create your model here.
class Comment(models.Model):
  owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
  comment = models.CharField(max_length=4000)
  comment_image = models.ImageField(upload_to="comment_image", null=True, blank=True)
  comment_date = models.DateField(auto_now_add=True)

  def __str__(self):
    return self.comment