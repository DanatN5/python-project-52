from django.contrib import admin

from task_manager.apps.task.models import Task

admin.site.register(Task)
