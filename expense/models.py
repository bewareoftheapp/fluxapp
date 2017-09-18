'''Expense models.'''


from django.contrib.auth.models import User
from django.db import models


def get_as_request_data(requests):
    '''Map any request list to RequestData list.'''
    return [RequestData(x) for x in requests]


def truncate_long_string(text):
    '''Truncate long string or return full short strings.'''
    return text if len(text) < 15 else text[0:12] + "..."


class Request(models.Model):
    '''Represent a generic request in the app.'''

    requester = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return str(self.requester)


class Budget(Request):
    '''Represent a budget request.'''

    value = models.FloatField(null=False)
    description = models.TextField(null=True)

    def __str__(self):
        return truncate_long_string(str(self.description))


class Reimburse(Request):
    '''Represent a reimburse request.'''

    value = models.FloatField(null=False)
    description = models.TextField(null=True)

    def __str__(self):
        return truncate_long_string(str(self.description))


class Approval(models.Model):
    '''Represent a request approval.'''

    approver = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(null=False)
    timestamp = models.DateTimeField(auto_now=True, null=False)
    message = models.CharField(max_length=350, null=True)
    request = models.ForeignKey(Request, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return "approved" if self.status else "denied"


class Commentary(models.Model):
    '''Represent a request commentary.'''

    request = models.ForeignKey(Request, null=False)
    timestamp = models.DateTimeField(auto_now=True, null=False)
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    text = models.TextField(null=False)

    def __str__(self):
        return truncate_long_string(str(self.text))


class RequestData(object):
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
        self.commentary_set = request.commentary_set.all().order_by('timestamp')

        try:
            self.approval = request.approval_set.latest('timestamp')
        except Approval.DoesNotExist:
            self.approval = None
