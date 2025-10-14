from django.db import models
from django.db.models import ProtectedError


class Label(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        if self.task.exists():
            raise ProtectedError(f'Label {self.name} is in use. You cannot delete it',
                                 self.task.all())
        super().delete(*args, **kwargs)
        


    def __str__(self):
        return self.name