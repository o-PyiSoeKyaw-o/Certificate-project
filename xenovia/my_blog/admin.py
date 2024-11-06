from django.contrib import admin
from my_blog.models import PostModel, CommentModel, UserDetailModel, Category, CategoryDetail
# Register your models here.
# admin.site.register(PostModel)
    
class PostModelAdmin(admin.ModelAdmin):
    list_display = ("title","body","created_at")
    list_filter = ("created_at",)
    search_field = ("title","body",)

admin.site.register(PostModel)
admin.site.register(CommentModel)
admin.site.register(UserDetailModel)
admin.site.register(Category)
admin.site.register(CategoryDetail)