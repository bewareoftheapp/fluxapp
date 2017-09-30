'''Register models for admin site.'''


import user.models as UserModels

from django.contrib import admin

import expense.models as ExpenseModels


admin.site.register(ExpenseModels.Reimburse)
admin.site.register(UserModels.Department)
admin.site.register(UserModels.RegistrationToken)
