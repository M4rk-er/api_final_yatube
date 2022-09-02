from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

v1router = routers.DefaultRouter()
v1router.register('posts', PostViewSet, basename='posts')
v1router.register('groups', GroupViewSet, basename='groups')
v1router.register(
    r'posts/(?P<post_id>[\d]+)/comments',
    CommentViewSet,
    basename='comments'
)
v1router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(v1router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
