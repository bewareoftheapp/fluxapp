from django.contrib.auth.models import User as UserModel
from django.db import models


class Department(models.Model):
    '''Represent a department.'''

    name = models.CharField(max_length=128)

    def __str__(self):
        return str(self.name)


class UserDepartmentRelation(models.Model):
    '''Relates an user and a department.'''

    user = models.ForeignKey(UserModel)
    department = models.ForeignKey(Department)
    leader = models.BooleanField(default=False)
