from django.db import models

# Create your models here.
class Shlok(models.Model):
    title = models.CharField(max_length=150)
    shlok = models.TextField()
    meaning = models.TextField()