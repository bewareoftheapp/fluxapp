from django.db import models

from user.models import User


class Budget(models.Model):

    requester = models.ForeignKey(User)
    value = models.FloatField()
    description = models.TextField()


class Reimburse(models.Model):

    requester = models.ForeignKey(User)
    value = models.ForeignKey(Budget)
    description = models.TextField()
