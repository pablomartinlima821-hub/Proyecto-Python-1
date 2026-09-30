from django.contrib import admin
from .models import Project, Tag, Task
 
admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Tag)

# Register your models here.
