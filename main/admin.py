from django.contrib import admin
from .models import Blog, BlogCatagory, BlogSeries
from tinymce.widgets import TinyMCE
from django.db import models

class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title and Publisher', {'fields': ['title', 'publisher']}),
        ('Date of publication', {'fields': ['published']}),
        ('URL', {'fields': ['slug']}),
        ('Series', {'fields': ['blog_series']}),
        ('Content', {'fields': ['content']})
        
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }
admin.site.register(BlogCatagory)
admin.site.register(BlogSeries)
admin.site.register(Blog, BlogAdmin)