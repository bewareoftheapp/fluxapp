from django.contrib.auth.models import User
from django.db import models


def get_as_request_data(requests):
    return [RequestData(x) for x in requests]


class Request(models.Model):

    requester = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True, null=False)


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


class RequestData:

    def __init__(self, request):
        if issubclass(type(request), Budget):
            self.request_type = 'budget'
        elif issubclass(type(request), Reimburse):
            self.request_type = 'reimburse'
        else:
            raise TypeError("RequestData: not a Budget nor a Reimburse.")

        self.requester = request.requester
        self.timestamp = request.timestamp
        self.value = request.value
        self.description = request.description

        try:
            self.approval = request.approval_set.latest('timestamp')
        except Approval.DoesNotExist:
            self.approval = None
