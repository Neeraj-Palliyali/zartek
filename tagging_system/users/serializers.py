from rest_framework import serializers

from administrator.models import Image, Post
from utils.get_tags import tag_list

class PostSerializer(serializers.Serializer):
    class meta:
        model= Post 
        exclude = ('updated_at', )

    def to_representation(self, instance):

        repressentation = super().to_representation(instance)
        repressentation['id'] = instance.id
        repressentation['caption'] = instance.name        
        repressentation['description'] = instance.description     
        repressentation['tags'] = tag_list(instance)
        repressentation['created_at'] = instance.created_at.strftime("%m/%d/%Y, %H:%M")
        images = Image.objects.filter(post = instance.id)
        repressentation['images'] = [str(image.image.url) for image in images]
        return repressentation



class PostLikeSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()
    status = serializers.BooleanField()
    
    def validate(self, attrs):
        if not Post.objects.filter(id = attrs['post_id']):
            raise serializers.ValidationError("The post you are trying to like does not exist")
        return super().validate(attrs)