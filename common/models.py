from django.db import models
from django.contrib.auth.models import User

class Forest(models.Model):
    title = models.CharField(max_length=200)
    addr1 = models.TextField()
    addr2 = models.TextField()
    firstimage = models.ImageField(upload_to='images/',blank=True, null=True)

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    forest = models.ForeignKey(Forest, null=True, blank=True, on_delete=models.CASCADE)
    voter = models.ManyToManyField(User, related_name='voter_review')

class Comment2(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    review = models.ForeignKey(Review, null=True, blank=True, on_delete=models.CASCADE)
 