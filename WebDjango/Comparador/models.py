from django.db import models

# Create your models here.
class ModelCards (models.Model):
    
    link = models.IntegerField()
    image = models.IntegerField()
    description = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.link
