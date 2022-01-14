from rest_framework.routers import DefaultRouter
from posts.models.comment import Comment
from users.views import UserViewSet
from user_profile.views import ProfileViewSet
from posts.views.posts import PostViewSet
from posts.views.comments import CommentViewSet
from posts.views.votes import VoteViewSet
# from friend_requests import FriendRequestViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'profiles', ProfileViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'votes', VoteViewSet)
# router.register(r'friend_requests', )

urlpatterns = router.urls