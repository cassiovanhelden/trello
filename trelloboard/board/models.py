from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class BaseModel(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Status(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Projects(BaseModel):
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)


class Task(BaseModel):
    assignee_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='tasks')
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)
