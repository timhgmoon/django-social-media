from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from user_profile.permissions import IsOwnerOrReadOnly
from posts.serializers.post import PostSerializer
from ..models.post import Post

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
  
  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

