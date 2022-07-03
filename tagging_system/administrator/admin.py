from django.contrib import admin

from .models import Image, Post

class ImageAdmin(admin.TabularInline):
    model = Image
    list_display= ('post', )

    def post (self, obj):
        if obj.post.name:
            return obj.post.name
        else:
            return None

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = (
        'name',
        'tag_list',
    )
    inlines = [
        ImageAdmin,
    ]
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
        
admin.site.register(Post, PostAdmin)