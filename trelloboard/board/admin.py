from django.contrib import admin

from .models import Task, Projects, Status

admin.site.register(Task)
admin.site.register(Projects)
admin.site.register(Status)
