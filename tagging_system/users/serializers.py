from rest_framework import serializers

from administrator.models import Post

class PostSerializer(serializers.Serializer):
    class meta:
        model= Post 
        exclude = ('updated_at', )

    def to_representation(self, instance):

        repressentation = super().to_representation(instance)
        repressentation['caption'] = instance.name        
        repressentation['description'] = instance.description     
        repressentation['tags'] = tag_list(instance)
        repressentation['created_at'] = instance.created_at.strftime("%m/%d/%Y, %H:%M")
        return repressentation

def tag_list(obj):
    return u", ".join(o.name for o in obj.tags.all())

class PostLikeSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()
    status = serializers.BooleanField()
    
    def validate(self, attrs):
        if not Post.objects.filter(id = attrs['id']):
            raise serializers.ValidationError("The post you are trying to like does not exist")
        return super().validate(attrs)