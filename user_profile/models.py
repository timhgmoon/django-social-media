from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class UserProfile(models.Model):
  options = (
    ('male', 'Male'),
    ('female', 'Female'), 
    ('other', 'Others')
  )

  owner = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile_data')
  gender = models.CharField(
    max_length = 20,
    choices = options,
    default = 'male',
    null = False,
    blank = False
  )

  dob = models.DateField(null=True, blank=True, default=None)
  phone = models.CharField(max_length=20, null=True, blank=True)
  work = models.CharField(max_length=100, null=True, blank=True)
  location = models.CharField(max_length=100, null=True, blank=True)
  about = models.CharField(max_length=800, blank=True, null=True)
  profile_image=models.ImageField(upload_to="profile_image", null=True, blank=True)
  # friends = models.ManyToManyField(User, related_name='friends', blank=True)