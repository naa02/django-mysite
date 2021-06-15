from django.db import models
from django.contrib.auth.models import User

class Forest(models.Model):
    title = models.CharField(max_length=200)
    addr1 = models.TextField()
    addr2 = models.TextField()
    firstimage = models.ImageField(upload_to='images/',blank=True, null=True)