from django.db import models


# Create your models here.
class Resume(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
