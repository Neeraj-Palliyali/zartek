from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from administrator.models import Post
from users.serializers import PostLikeSerializer, PostSerializer
from .models import UserLiked
# Create your views here.
class UserPostsViewSet(viewsets.ModelViewSet):
    serializer_class= PostSerializer 
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = PostLikeSerializer(data= request.data)
        serializer.is_valid(raise_exception= True)
        data = serializer.data
        try:
            UserLiked.objects.create(
            user = request.user.id,
            postId = data['postId'],
            status = data['status']
            )
            stat = "liked" if data['status'] else "disliked"
            return Response(
                {
                "sucess":True,
                "message":stat
                }, 
                status= status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {
                    "success":False,
                    "message":"please check with admin"
                }
            )


    def list(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = self.serializer_class(posts, many = True).data
        return Response(
            {
                "success":True,
                "message": serializer
            },
            status= status.HTTP_200_OK
        )