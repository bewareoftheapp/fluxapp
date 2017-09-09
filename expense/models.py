'''Expense models.'''


from django.contrib.auth.models import User
from django.db import models


def get_as_request_data(requests):
    '''Map any request list to RequestData list.'''
    return [RequestData(x) for x in requests]


class Request(models.Model):
    '''Represent a generic request in the app.'''

    requester = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True, null=False)


class Budget(Request):
    '''Represent a budget request.'''

    value = models.FloatField(null=False)
    description = models.TextField(null=True)


class Reimburse(Request):
    '''Represent a reimburse request.'''

    value = models.FloatField(null=False)
    description = models.TextField(null=True)


class Approval(models.Model):
    '''Represent a request approval.'''

    approver = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(null=False)
    timestamp = models.DateTimeField(auto_now=True, null=False)
    message = models.CharField(max_length=350, null=True)
    request = models.ForeignKey(Request, null=False, on_delete=models.CASCADE)


class Commentary(models.Model):
    '''Represent a request commentary.'''

    request = models.ForeignKey(Request, null=False)
    timestamp = models.DateTimeField(auto_now=True, null=False)
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    text = models.TextField(null=False)


class RequestData:
    '''Collects request data to be rendered.'''

    def __init__(self, request):
        if issubclass(type(request), Budget):
            self.type = 'Verba'
        elif issubclass(type(request), Reimburse):
            self.type = 'Reembolso'
        else:
            raise TypeError("RequestData: not a Budget nor a Reimburse.")

        self.id = request.request_ptr_id
        self.requester = request.requester
        self.timestamp = request.timestamp
        self.value = request.value
        self.description = request.description
        self.approval_set = request.approval_set.all().order_by('-timestamp')

        try:
            self.approval = request.approval_set.latest('timestamp')
        except Approval.DoesNotExist:
            self.approval = None
