from django.db import models

# Create your models here.
class ModelCards (models.Model):
    
    link = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.link
