from django.db import models


class Resume(models.Model):
    description = models.CharField(max_length=200, default='404 ERROR NOT FOUND')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    file_image = models.ImageField(upload_to='images/')

    def __str__(self):
        name = self.first_name + self.last_name
        return name
