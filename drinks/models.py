from distutils.command.upload import upload
from email.policy import default
from django.db import models


class drink(models.Model):
    name=models.CharField(max_length=15)
    price=models.IntegerField()
    description=models.CharField(max_length=50)
    img=models.ImageField(upload_to='fruit/images',default='')
    def __str__(self):
        return(self.name)