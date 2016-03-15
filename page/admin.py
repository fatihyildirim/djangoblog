from django.contrib import admin
from page.models import Page


class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'content', 'status')
	prepopulated_fields = {'slug': ('title',)}


admin.site.register(Page, PageAdmin)