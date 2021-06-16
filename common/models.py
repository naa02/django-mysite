from django.db import models
from django.contrib.auth.models import User

class Forest(models.Model):
    title = models.CharField(max_length=200)
    addr1 = models.TextField()
    addr2 = models.TextField()
    firstimage = models.ImageField(upload_to='images/',blank=True, null=True)

    def __str__(self) :
        return self.title

class Comment2(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    forest = models.ForeignKey(Forest, null=True, blank=True, on_delete=models.CASCADE)
 