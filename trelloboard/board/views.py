from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from django.contrib.auth.models import User

from .models import Task, Projects, Status
from .serializers import TaskSerializer, UserSerializer, ProjectSerializer, TaskToDisplaySerializer, StatusSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskToDisplaySerializer


class TaskDetail(generics.RetrieveAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class ProjectList(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Projects.objects.all()


class ProjectDetail(generics.RetrieveAPIView):
    serializer_class = ProjectSerializer
    queryset = Projects.objects.all()


class StatusList(generics.ListCreateAPIView):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()


class StatusDetail(generics.RetrieveAPIView):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()

