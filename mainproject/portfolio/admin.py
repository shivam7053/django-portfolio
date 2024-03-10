# portfolio/admin.py
from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    readonly_fields = ('image_tag',)  # Include the image_tag method

admin.site.register(Project, ProjectAdmin)
