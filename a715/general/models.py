from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(default='')
    price = models.FloatField(default=0)
    is_available = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photos')

    def __str__(self):
        return f'{self.name} за {self.price}р'
