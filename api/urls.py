from rest_framework.routers import DefaultRouter
from django.urls import path, include
from users.views import SignIn, SignOut, SignUp
from user_profile.views import ProfileViewSet
from posts.views.posts import PostViewSet
from posts.views.comments import CommentViewSet
from posts.views.votes import VoteViewSet
# from friend_requests import FriendRequestViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'votes', VoteViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('sign-in/', SignIn.as_view(), name="sign-in"),
  path('sign-up/', SignUp.as_view(), name="sign-up"),
  path('sign-out/', SignOut.as_view(), name="sign-out")
]