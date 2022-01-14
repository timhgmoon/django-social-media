from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FriendRequest(models.Model):
  from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
  to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)
  
  def __str__(self):
    return f"{self.from_user} wants to be your friend!"
