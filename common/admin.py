from django.contrib import admin
from .models import Forest, Comment2

class ForestAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(Forest, ForestAdmin)

class Comment2Admin(admin.ModelAdmin):
    search_fields = ['content']

admin.site.register(Comment2, Comment2Admin)
