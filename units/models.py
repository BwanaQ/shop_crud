from django.db import models
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL


class Unit(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    occupied = models.BooleanField(default=False)
    image = models.ImageField(
        upload_to='musonge/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User, related_name='units', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
