from django.db import models



# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    text = models.TextField(default="Add your text here")
    image = models.ImageField(upload_to='events_images/')
