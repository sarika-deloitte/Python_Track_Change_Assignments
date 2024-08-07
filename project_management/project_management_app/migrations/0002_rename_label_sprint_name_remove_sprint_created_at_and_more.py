# Generated by Django 4.2.5 on 2024-08-06 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_management_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sprint',
            old_name='label',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='sprint',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='sprint',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='project',
            name='users',
            field=models.ManyToManyField(related_name='projects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sprint',
            name='users',
            field=models.ManyToManyField(related_name='sprints', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sprint',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sprints', to='project_management_app.project'),
        ),
    ]
