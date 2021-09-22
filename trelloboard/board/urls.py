from django.urls import path
from .views import TaskList, ProjectList, TaskDetail, ProjectDetail, StatusList, StatusDetail

urlpatterns = [
    path('tasks/', TaskList.as_view()),
    path('tasks/<int:pk>/', TaskDetail.as_view()),
    path('projects/', ProjectList.as_view()),
    path('projects/<int:pk>/', ProjectDetail.as_view()),
    path('status/', StatusList.as_view()),
    path('status/<int:pk>/', StatusDetail.as_view()),
]

