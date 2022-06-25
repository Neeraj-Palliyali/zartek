from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import  BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import PostSerializer
# Create your views here.

class PostsViewSets(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
    def list(self, request, *args, **kwargs):
        return Response("hehe")
