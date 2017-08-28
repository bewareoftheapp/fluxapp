from django.contrib.auth.models import User
from django.db import models


class Request(models.Model):

    requester = models.ForeignKey(User, null=False, on_delete=models.CASCADE)


class Budget(Request):

    value = models.FloatField(null=False)
    description = models.TextField(null=True)


class Reimburse(Request):

    value = models.FloatField(null=False)
    description = models.TextField(null=True)


class Approval(models.Model):

    approver = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(null=False)
    timestamp = models.DateTimeField(auto_now=True, null=False)
    message = models.CharField(max_length=350, null=True)
    request = models.ForeignKey(Request, null=False, on_delete=models.CASCADE)


class Commentary(models.Model):

    request = models.ForeignKey(Request, null=False)
    timestamp = models.DateTimeField(auto_now=True, null=False)
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    text = models.TextField(null=False)
