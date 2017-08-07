from django.db import models


class Budget(models.Model):

    requestester = models.ForeignKey('user')
    value = models.FloatField()
    description = models.TextField()


class Reimburse(models.Model):

    requestester = models.ForeignKey('user')
    budget = models.ForeignKey(Budget)
