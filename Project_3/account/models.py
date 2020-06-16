from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser


class ProUser(AbstractUser):
    image = models.ImageField(default='default.jpg', upload_to='pics', null=True, blank=True)
    avr_score = models.IntegerField(null=True, blank=True)
