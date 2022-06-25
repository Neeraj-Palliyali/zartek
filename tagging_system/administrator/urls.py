from django.db import router
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import PostsViewSets

router = DefaultRouter(trailing_slash = False)

router.register(r"posts", PostsViewSets, basename="posts")

urlpatterns = [
    path('api/', include(router.urls))
]
