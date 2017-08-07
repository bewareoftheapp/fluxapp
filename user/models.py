from django.db import models


class User(models.Model):

    group = models.ForeignKey(Group)


class Group(models.Model):

    name = models.CharField()
