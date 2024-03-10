# portfolio/models.py
from django.db import models
from django.utils.html import escape, mark_safe

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe(f'<img src="{escape(self.image.url)}" width="150" height="150" />')

    image_tag.short_description = 'Image'
