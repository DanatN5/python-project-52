from django.conf import settings
from django.db import models

from task_manager.apps.status.models import Status
from task_manager.apps.label.models import Label


class Task(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='author')
    
    executor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='executor')
    
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name='status')
    
    label = models.ManyToManyField(
        Label,
        related_name='labels')

    def __str__(self):
        return self.name