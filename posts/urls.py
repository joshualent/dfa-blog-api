from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import UserViewSet, PostViewSet

router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("", PostViewSet, basename="posts")

urlpatterns = router.urls


# from .views import postlist, postdetail, userlist, userdetail

# urlpatterns = [
#     path("users/", userlist.as_view(), name="user_list"),
#     path("users/<int:pk>/", userdetail.as_view(), name="user_detail"),
#     path("<int:pk>/", postdetail.as_view(), name="post_detail"),
#     path("", postlist.as_view(), name="post_list"),
# ]
