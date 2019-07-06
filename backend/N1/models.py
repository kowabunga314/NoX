from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserCreated(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True

