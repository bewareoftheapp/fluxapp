'''Register models for admin site.'''


import user.models as UserModels

from django.contrib import admin

import department.models as DepartmentModels
import expense.models as ExpenseModels

admin.site.register(ExpenseModels.Reimburse)
admin.site.register(DepartmentModels.Department)
admin.site.register(DepartmentModels.UserDepartmentRelation)
admin.site.register(UserModels.RegistrationToken)
