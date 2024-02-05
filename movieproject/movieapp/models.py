from django.db import models


# Create your models here.


class Movietb(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField()
    year = models.IntegerField(null=True,blank=True)
    image = models.ImageField(upload_to="movies", null=True, blank=True)

    def __str__(self):
        return self.name
