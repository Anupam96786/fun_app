from django.db import models
from django.contrib.auth.models import User

class Relation(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    love1 = models.CharField(max_length=20)
    love2 = models.CharField(max_length=20)

