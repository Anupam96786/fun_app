from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=1200)
    def __str__(self):
        return self.message
    
