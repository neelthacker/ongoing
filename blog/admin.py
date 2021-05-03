from django.contrib import admin
from .models import Post, Category, Comments

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ['title']
    
admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Comments)