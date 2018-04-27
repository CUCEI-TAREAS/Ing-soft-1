from django.db import models

# Create your models here.

class User(models.Model):
    code_user = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
