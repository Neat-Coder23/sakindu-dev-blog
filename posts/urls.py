from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_list, name='posts_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('new/', views.post_new, name='post_new'),
]