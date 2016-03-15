from django.contrib import admin
from app.models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'status')
	prepopulated_fields = {'slug' : ('title',)}


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'status')
	prepopulated_fields = {'slug' : ('name',)}


class TagAdmin(admin.ModelAdmin):
	list_display = ('name', 'status')
	prepopulated_fields = {'slug' : ('name',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)