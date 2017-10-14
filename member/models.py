from django.db import models

# Create your models here.
class Member(models.Model):
    '''Church member model.'''

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)
    facebook = models.URLField(max_length=256)
