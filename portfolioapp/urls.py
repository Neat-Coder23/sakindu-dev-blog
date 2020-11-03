from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects_list, name='projects_list'),
    path('<int:pk>', views.project_detail, name='project_detail'),
    path('new/', views.new_project, name='new_project'),
]