from django.contrib import admin

from loan.models import *


@admin.register(LoanApplication)
class LoanApplication(admin.ModelAdmin):
    pass


@admin.register(LoanCreditScore)
class LoanCreditScore(admin.ModelAdmin):
    pass


@admin.register(LoanApplicationSpouseProfile)
class LoanApplicationSpouseProfile(admin.ModelAdmin):
    pass


@admin.register(LoanCurrentJobs)
class LoanCurrentJobs(admin.ModelAdmin):
    pass


@admin.register(LoanApplicationVerification)
class LoanApplicationVerification(admin.ModelAdmin):
    pass


@admin.register(LoanAppraisalCollateral)
class LoanAppraisalCollateral(admin.ModelAdmin):
    pass


@admin.register(LoanMarginConfigurable)
class LoanMarginConfigurable(admin.ModelAdmin):
    pass


@admin.register(LoanApproval)
class LoanApproval(admin.ModelAdmin):
    pass