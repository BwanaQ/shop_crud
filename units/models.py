from django.db import models

# Create your models here.


class Unit(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    occupied = models.BooleanField(default=False)
    image = models.ImageField(
        upload_to='musonge/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
