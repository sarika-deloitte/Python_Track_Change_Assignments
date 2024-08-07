from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone
class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.username

class Project(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    end_date = models.DateField(default=timezone.now)  
    users = models.ManyToManyField(CustomUser, related_name='projects')

    def __str__(self):
        return self.name

class Sprint(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='sprints')
    users = models.ManyToManyField(CustomUser, related_name='sprints')

    def __str__(self):
        return self.name