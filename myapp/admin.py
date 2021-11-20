from django.contrib import admin
from .models import Blog #markdown追加
from markdownx.admin import MarkdownxModelAdmin #markdown追加

# Register your models here.
admin.site.register(Blog,MarkdownxModelAdmin) #markdown追加