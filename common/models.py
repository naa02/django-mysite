from django.db import models

# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     content = models.TextField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
#     image = models.ImageField(upload_to='images/',blank=True, null=True)
    
#     def __str__(self):
#         return self.title

# class Photo(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
#     image = models.ImageField(upload_to='images/', blank=True, null=True)