from django.db import models

# Create your models here.
class job(models.Model):   #model class
    image = models.ImageField(upload_to='image')
    summary = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    year = models.TextField

    def __str__(self):
        return self.summary


