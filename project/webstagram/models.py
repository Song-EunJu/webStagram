from django.db import models

# Create your models here.
class Instagram(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    # image = models.ImageField(upload_to = "blog/", blank = True, null = True)
