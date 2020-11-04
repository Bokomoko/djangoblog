from django.contrib import admin

# Register your models here.
# Place here models that Admin may  create, add, edit, delete entities
from .models import Post


# @admin same as admin.site ... to shorten
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display  = ("title","slug","author","created","updated")
    prepopulated_fields = {"slug":("title",)}