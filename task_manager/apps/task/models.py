from django.conf import settings
from django.db import models

from task_manager.apps.label.models import Label
from task_manager.apps.status.models import Status


class Task(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='author',
        verbose_name='Автор')
    
    executor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='executor',
        verbose_name='Исполнитель')
    
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name='status',
        verbose_name='Статус')
    
    label = models.ManyToManyField(
        Label,
        related_name='labels',
        verbose_name='Метки')

    def __str__(self):
        return self.name