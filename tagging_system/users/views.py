from django.db.models import Q

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from administrator.models import Post
from utils.pagination import PostPagination
from users.serializers import PostLikeSerializer, PostSerializer
from .models import UserLiked
# Create your views here.
class UserPostsViewSet(viewsets.ModelViewSet):
    serializer_class= PostSerializer 
    permission_classes = (IsAuthenticated,)
    pagination_class = PostPagination

    def create(self, request, *args, **kwargs):
        serializer = PostLikeSerializer(data= request.data)
        serializer.is_valid(raise_exception= True)
        data = serializer.data
        try:
            like = UserLiked.objects.get(
                user_id = request.user.id,
                postId_id = data['post_id']
                )
            like.like_status = data['status']
            like.save()
            stat = "liked" if data['status'] else "disliked"
            
            return Response(
                {
                "sucess":True,
                "message":stat
                }, 
                status= status.HTTP_201_CREATED
            )
        except UserLiked.DoesNotExist:
            return Response(
                {
                    "success":False,
                    "message":"Liked something you didn't view"
                },
                status= status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {
                    "success":False,
                    "message":str(e)
                },
                status= status.HTTP_400_BAD_REQUEST
            )


    def list(self, request, *args, **kwargs):
        # user_id = request.user.id
        # liked = UserLiked.objects.filter(user_id = user_id,)
        # if liked:
        #     tags = []
        #     for like in liked:
        #         tags 
        #     return Response(
        #     {
        #         "success":True,
        #         "message": "hehe"
        #     },
        #     status= status.HTTP_200_OK
        # )
        user_id = request.user
        viewed = UserLiked.objects.filter(user = user_id).values_list('postId', flat= True)
        if not viewed:
            posts = Post.objects.all()
            print("here")
        else:
            viewed = list(viewed)
            print(viewed)
            posts = Post.objects.filter(~Q(pk__in = viewed))
            print(posts)
        if posts:
            page = self.paginate_queryset(posts)
            if page is not None:
                serializer = self.serializer_class(page, many = True).data
                for post in serializer:
                    print(posts.filter(id= post.get('id')))
                    UserLiked.objects.create(
                    user = user_id,
                    postId = posts.get(id= post.get('id')),
                    )
                page_data = self.get_paginated_response(serializer).data
                return Response(
                    {
                        "success":True,
                        "message": page_data
                    },
                    status= status.HTTP_200_OK
                )
        else:
            return Response(
                    {
                        "success":True,
                        "message": "No new posts!!"
                    },
                    status= status.HTTP_200_OK
                )