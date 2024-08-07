from rest_framework import serializers
from .models import User, Project, Sprint

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active', 'date_joined']

class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'start_date', 'created_at', 'updated_at', 'users']

class SprintSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Sprint
        fields = ['id', 'name', 'start_date', 'end_date', 'project', 'users']
