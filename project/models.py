from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    body = models.TextField()
    cover = models.ImageField(upload_to='images/', null=True)
    # do I need a date field for each post? 

    def __str__(self):
        return self.title