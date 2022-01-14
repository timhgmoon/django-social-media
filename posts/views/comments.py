from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from ..models.comment import Comment
from ..serializers.comment import CommentSerializer
from user_profile.permissions import IsOwnerOrReadOnly

#create your views here.
class CommentViewSet(viewsets.ModelViewSet):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  permission_class=[permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)