from django.contrib import admin

from account.models import *


# Register your models here.
@admin.register(AccountProfile)
class AccountProfile(admin.ModelAdmin):
    pass


@admin.register(AccountBankUsers)
class AccountBankUsers(admin.ModelAdmin):
    pass


@admin.register(AccountReplicationProfile)
class AccountReplicationProfile(admin.ModelAdmin):
    pass


@admin.register(AccountPasswordExpired)
class AccountPasswordExpired(admin.ModelAdmin):
    pass


@admin.register(AccountLogResetPassword)
class AccountLogResetPassword(admin.ModelAdmin):
    pass


@admin.register(AccountLogChangePassword)
class AccountLogChangePassword(admin.ModelAdmin):
    pass


@admin.register(AccountUserPin)
class AccountUserPin(admin.ModelAdmin):
    pass


@admin.register(AccountMemberVerifyStatus)
class AccountMemberVerifyStatus(admin.ModelAdmin):
    pass