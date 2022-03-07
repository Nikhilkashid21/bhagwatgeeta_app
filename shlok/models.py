from django.db import models

# Create your models here.
class Adhyay(models.Model):
    title = models.CharField(max_length=100)

class Shlok(models.Model):
    title = models.CharField(max_length=150)
    shlok = models.TextField()
    meaning = models.TextField()
    adhyay= models.ForeignKey(Adhyay,on_delete=models.CASCADE)