from django.db import models


# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255)
    publication_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:100]

    def pub_date_rounded(self):
        return self.publication_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title


