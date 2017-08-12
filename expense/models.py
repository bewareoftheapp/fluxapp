from django.db import models

from user.models import User


class Budget(models.Model):

    requestester = models.ForeignKey(User)
    value = models.FloatField()
    description = models.TextField()


class Reimburse(models.Model):

    requestester = models.ForeignKey(User)
    budget = models.ForeignKey(Budget)
