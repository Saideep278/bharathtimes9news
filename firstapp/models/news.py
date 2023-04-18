from django.db import models
from django.db.models import Model


class News(models.Model):
    title = models.CharField(max_length=50)
    tagline = models.CharField(max_length=250,default='', null = True, blank = True )
    desc = models.TextField()
    category = models.CharField(max_length=50)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    #image = models.ImageField(upload_to='uploads/products')
    media = models.FileField(upload_to='media')


    @staticmethod
    def news_by_id(ids):
        return News.objects.filter(id__in=ids)
