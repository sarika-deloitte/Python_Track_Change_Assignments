# urls.py

from django.urls import path
from . import views
from .views import user_list, user_create, user_update, user_delete, user_detail
from .views import project_list, project_create, project_update, project_delete, project_detail
from .views import sprint_list, sprint_create, sprint_update, sprint_delete, sprint_detail


urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<int:pk>/update/', views.user_update, name='user_update'),
    path('users/<int:pk>/delete/', views.user_delete, name='user_delete'),
    
    path('projects/', views.project_list, name='project_list'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<int:pk>/update/', views.project_update, name='project_update'),
    path('projects/<int:pk>/delete/', views.project_delete, name='project_delete'),
    
    path('sprints/', views.sprint_list, name='sprint_list'),
    path('sprints/create/', views.sprint_create, name='sprint_create'),
    path('sprints/<int:pk>/update/', views.sprint_update, name='sprint_update'),
    path('sprints/<int:pk>/delete/', views.sprint_delete, name='sprint_delete'),
    
    path('sprints/<int:pk>/', views.sprint_detail, name='sprint_detail'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('users/<int:pk>/', views.user_detail, name='users_detail'),
]
