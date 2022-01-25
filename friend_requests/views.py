from django.shortcuts import render
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import FriendRequestSerializer
from .models import FriendRequest
from django.shortcuts import get_object_or_404

# Create your views here.
