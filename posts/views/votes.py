from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status, permissions, serializers
from ..models.vote import Vote
from ..serializers.vote import VoteSerializer
from ..permissions import HasSelfVotedOrReadOnly


#Create your views here
class VoteViewSet(viewsets.ModelViewSet):
  queryset = Vote.objects.all()
  serializer_class = VoteSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, HasSelfVotedOrReadOnly]

  def perform_create(self, serializer):
    post_instance = get_object_or_404(Post, pk=self.request.data['post'])
    #if user likes the post else if user dislikes
    if self.request.data['up_vote']:
      already_up_voted = Vote.objects.filter(post=post_instance, up_voted_by=self.request.user).exists()
      if already_up_voted:
        raise serializers.ValidationError({"message": "You have already liked this post"})
      else:
        serializer.save(up_voted_by=self.request.user, post=post_instance)
    else:
      already_down_voted = Vote.objects.filter(post=post_instance, down_voted_by=self.request.user).exists()
      if already_down_voted:
        raise serializers.ValidationError({"message": "You have already liked this post"})
      else:
        serializer.save(down_voted_by=self.request.user, post=post_instance)


    return super().perform_create(serializer)
