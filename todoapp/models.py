from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=255)
    time = models.TimeField(auto_now=False, auto_now_add=False,blank=True, null=True)

    def __str__(self):
        return self.task