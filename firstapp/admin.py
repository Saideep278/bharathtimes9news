from django.contrib import admin
from .models.news import News

# Register your models here.

class AdminDNews(admin.ModelAdmin):
    list_display = ['title' ,'tagline', 'desc' ,'category', 'time','media']

admin.site.register(News,AdminDNews)

