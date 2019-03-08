from django.db import models
from datetime import datetime

class BlogCatagory(models.Model):
    blog_catagory = models.CharField(max_length=200)
    catagory_summery = models.CharField(max_length=200)
    catagory_slug = models.CharField(max_length=200, default=1)

    class Meta:
        verbose_name_plural = 'Catagories'
    
    def __str__(self):
        return self.blog_catagory

class BlogSeries(models.Model):
    blog_series = models.CharField(max_length=200)
    blog_catagory = models.ForeignKey(BlogCatagory, default = 1, verbose_name='Catagory', on_delete = models.SET_DEFAULT)
    series_summery = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Series'
    
    def __str__(self):
        return self.blog_series


class Blog(models.Model):
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateTimeField('date published', default = datetime.now())

    blog_series = models.ForeignKey(BlogSeries, default = 1, verbose_name='Series', on_delete = models.SET_DEFAULT)
    slug = models.CharField(max_length=200, default = 1)

    def __str__(self):
        return self.title
