from django.db import models
from django.contrib import admin

# Create your models here.

class BlogPost(models.Model):
    body        = models.TextField()
    title       = models.CharField(max_length=150)
    created     = models.DateTimeField()    
    class Meta:
        ordering = ('-created',)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created','body')
    
    
admin.site.register(BlogPost, BlogPostAdmin)