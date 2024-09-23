from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    affiliate = models.BooleanField(default=False)

class Preference(models.Model):
    user = models.ForeignKey(User, related_name='preferences', on_delete=models.CASCADE)
    preference = models.CharField(max_length=100)
