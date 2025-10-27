from django.contrib.auth import get_user_model
from django.db import models

from task_manager.apps.labels.models import Label
from task_manager.apps.statuses.models import Status

User = get_user_model()


class Task(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='author',
        verbose_name='Автор')
    
    executor = models.ForeignKey(
        User,
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
    
    labels = models.ManyToManyField(
        Label,
        blank=True,
        related_name='labels',
        verbose_name='Метки')

    def __str__(self):
        return self.name