from django.contrib import admin

from transaction.models import *


# Register your models here.
@admin.register(TransactionDepositTransit)
class TransactionDepositTransit(admin.ModelAdmin):
    pass


@admin.register(TransactionDepositVerified)
class TransactionDepositVerified(admin.ModelAdmin):
    pass


@admin.register(TransactionDepositTimeTransit)
class TransactionDepositTimeTransit(admin.ModelAdmin):
    pass