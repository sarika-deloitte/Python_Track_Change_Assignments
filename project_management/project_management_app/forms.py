from django import forms
from .models import CustomUser, Project, Sprint

class CustomUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

class ProjectForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(
        queryset=CustomUser.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # or use forms.SelectMultiple for a dropdown
        required=False  # if you want to make this field optional
    )

    class Meta:
        model = Project
        fields = ['name', 'start_date', 'end_date', 'users']  # In

class SprintForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(
        queryset=CustomUser.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # or use forms.SelectMultiple for a dropdown
        required=False
    )
    class Meta:
        model = Sprint
        fields = ['name', 'start_date', 'end_date', 'project', 'users']
