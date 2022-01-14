from rest_framework import serializers

from ..models.post import Post
from .comment import CommentSerializer
from .vote import VoteSerializer

class PostSerializer(serializers.ModelSerializer):
  comments = CommentSerializer(many=True, read_only=True)
  votes = VoteSerializer(many=True, read_only=True)
  class Meta:
    model = Post
    fields = ('id', 'content', 'post_image', 'category', 'post_date', 'comments', 'votes')
