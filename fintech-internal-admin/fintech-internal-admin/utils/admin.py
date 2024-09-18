from django.contrib import admin
from utils.models import *


# Register your models here.
@admin.register(Banks)
class Banks(admin.ModelAdmin):
    pass


@admin.register(Province)
class Province(admin.ModelAdmin):
    pass


@admin.register(District)
class District(admin.ModelAdmin):
    pass


@admin.register(SubDistrict)
class SubDistrict(admin.ModelAdmin):
    pass


@admin.register(LogNodeflux)
class LogNodeflux(admin.ModelAdmin):
    pass