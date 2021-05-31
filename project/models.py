from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    body = models.TextField()
    # image = look into adding an image field
    # do I need a date field for each post? 

    def __str__(self):
        return self.title