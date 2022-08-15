from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField('Car name', max_length=30)
    about = models.TextField('Car about')
    price = models.IntegerField('Car price')
    img = models.ImageField('Car image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'
