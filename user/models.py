from django.contrib.auth.models import User as UserModel
from django.db import models


class Group(models.Model):

    name = models.CharField(max_length=128)


class User(UserModel):

    group = models.ForeignKey(Group)
