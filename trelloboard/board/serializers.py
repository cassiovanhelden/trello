from rest_framework import serializers, status
from django.contrib.auth.models import User
from rest_framework.response import Response

from .models import Projects, Status, Task


class StatusSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    color = serializers.CharField(max_length=255)

    class Meta:
        model = Status
        fields = ['id', 'name', 'color']


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)

    class Meta:
        fields = ['email', 'username']
        model = User


class ProjectSerializer(serializers.ModelSerializer):
    owner_id = UserSerializer()
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    tasks = serializers.SerializerMethodField()

    class Meta:
        model = Projects
        fields = ['owner_id', 'title', 'description', 'tasks']

    def create(self, validated_data):
        owner_data = validated_data.pop('owner')
        try:
            owner = User.objects.get(email=owner_data['email'])
        except User.DoesNotExist:
            return Response("User doesn't exists", status=status.HTTP_404_NOT_FOUND)
        project = Projects.objects.create(owner=owner, **validated_data)
        return project

    def get_tasks(self, obj):
        qs = obj.tasks.all()
        return TaskSerializer(qs, many=True).data


class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    project_id = serializers.CharField(max_length=255)
    status_id = StatusSerializer()
    assignee_id = UserSerializer()

    class Meta:
        model = Task
        fields = ['title', 'description', 'project_id', 'status_id', 'assignee_id']


class TaskToDisplaySerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    project_id = ProjectSerializer()
    status_id = StatusSerializer()
    assignee_id = UserSerializer()

    class Meta:
        model = Task
        fields = ['title', 'description', 'project_id', 'status_id', 'assignee_id']
