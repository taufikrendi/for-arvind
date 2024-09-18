from django.contrib import admin

from deposits.models import *


# Register your models here.
@admin.register(DepositMemberPrincipal)
class DepositMemberPrincipal(admin.ModelAdmin):
    pass


@admin.register(DepositMemberMandatory)
class DepositMemberMandatory(admin.ModelAdmin):
    pass