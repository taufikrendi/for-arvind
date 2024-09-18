from django.contrib import admin

from deposits.models import *


# Register your models here.
@admin.register(DepositMemberPrincipal)
class DepositMemberPrincipalAdmin(admin.ModelAdmin):
    pass


@admin.register(DepositMemberMandatory)
class DepositMemberMandatoryAdmin(admin.ModelAdmin):
    pass


@admin.register(DepositProductMaster)
class DepositProductMasterAdmin(admin.ModelAdmin):
    pass


@admin.register(DepositMemberCurrent)
class DepositMemberCurrentAdmin(admin.ModelAdmin):
    pass