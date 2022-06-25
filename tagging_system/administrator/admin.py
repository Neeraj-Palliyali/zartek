from django.contrib import admin

from .models import Image, Post


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display= ('name',)

class ImageAdmin(admin.ModelAdmin):
    model = Image
    list_display= ('post',)

    def post (self, obj):
        if obj.post.name:
            return obj.post.name
        else:
            return None

admin.site.register(Image, ImageAdmin)
admin.site.register(Post, PostAdmin)