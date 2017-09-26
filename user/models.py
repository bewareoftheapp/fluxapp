'''User models.'''


import hashlib
import random
import string

from django.contrib.auth.models import User as UserModel
from django.core.urlresolvers import reverse
from django.db import models


def _generate_token():
    rand_str = str.encode(
        ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)]))
    token = hashlib.sha1()
    token.update(rand_str)
    return token.hexdigest()

# TODO Create a department leadership class.


class Department(models.Model):
    '''Represent a department.'''

    name = models.CharField(max_length=128)
    members = models.ForeignKey(UserModel)

    def __str__(self):
        return str(self.name)


class RegistrationToken(models.Model):
    '''Produce tokens for new accounts.'''

    token = models.CharField(null=False, max_length=40, default=_generate_token)
    email = models.EmailField(null=False)
    active = models.BooleanField(null=False, default=True)

    def url(self):
        '''Generate user registration URL.'''
        return reverse('register_user') + "?token={0}".format(self.token)
