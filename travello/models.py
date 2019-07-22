from django.db import models


class Destination(models.Model):
    name  = models.CharField(max_length=100,default="")
    price = models.IntegerField(default=0)
    img   = models.ImageField(upload_to='pics',default=0)
    desc  = models.TextField(default="")
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name

