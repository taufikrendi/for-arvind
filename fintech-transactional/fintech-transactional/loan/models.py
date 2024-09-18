from django.utils import timezone
from django.contrib.postgres.functions import RandomUUID
from django.db import models


class LoanApplication(models.Model):
    loan_application_id = models.UUIDField(
        primary_key=True, default=RandomUUID, editable=False, unique=True)
    loan_application_user_related = models.CharField(max_length=255, null=False, editable=False)
    loan_application_code_related = models.CharField(max_length=255, null=False, editable=False)
    loan_application_type_usage = models.CharField(max_length=50, null=False, editable=False)
    loan_application_amount = models.DecimalField(
        editable=False, null=False, max_digits=30, decimal_places=12, default=0)
    loan_application_installment_month = models.DecimalField(
        editable=False, null=False, max_digits=3, decimal_places=0, default=0)
    loan_application_reason = models.TextField(null=False)
    loan_application_collateral = models.TextField(null=False)
    loan_application_collateral_evident = models.TextField(null=False)
    loan_application_link_url = models.TextField(null=True)
    loan_application_create_by = models.CharField(max_length=255, null=False, editable=False)
    loan_application_created_date = models.DateTimeField(editable=False, null=False, auto_now_add=True)

    def __str__(self):
        return self.loan_application_user_related

    def __unicode__(self):
        return '%s' % self.loan_application_user_related

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.loan_application_id), escape(self.loan_application_user_related),
            escape(self.loan_application_type_usage), escape(self.loan_application_link_url),
            escape(self.loan_application_amount), escape(self.loan_application_installment_month),
            escape(self.loan_application_reason), escape(self.loan_application_collateral),
            escape(self.loan_application_create_by), escape(self.loan_application_created_date)
        )

    class Meta:
        ordering = ('loan_application_id',)
        indexes = [
            models.Index(
                fields=['loan_application_id',
                        'loan_application_user_related']), ]


class LoanCreditScore(models.Model):
    loan_credit_score_id = models.UUIDField(
        primary_key=True, default=RandomUUID, editable=False, unique=True)
    loan_credit_score_user_related = models.CharField(max_length=255, null=False, editable=False)
    loan_credit_score_application_code_related = models.CharField(max_length=255, null=False, editable=False)
    loan_credit_score_result_from_clik_trx_id = models.CharField(max_length=255, null=False, editable=False)
    loan_credit_score_result_from_clik = models.JSONField(null=True, editable=False)
    loan_credit_score_create_by = models.CharField(max_length=255, null=False, editable=False)
    loan_credit_score_created_date = models.DateTimeField(editable=False, null=False, auto_now_add=True)

    def __str__(self):
        return self.loan_credit_score_user_related

    def __unicode__(self):
        return '%s' % self.loan_credit_score_user_related

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.loan_credit_score_id), escape(self.loan_credit_score_user_related),
            escape(self.loan_credit_score_application_code_related), escape(self.loan_application_installment_month),
            escape(self.loan_application_reason), escape(self.loan_credit_score_result_from_clik_trx_id),
            escape(self.loan_credit_score_result_from_clik), escape(self.loan_credit_score_create_by),
            escape(self.loan_credit_score_created_date)
        )

    class Meta:
        ordering = ('loan_credit_score_id',)
        indexes = [
            models.Index(
                fields=['loan_credit_score_id',
                        'loan_credit_score_user_related',
                        'loan_credit_score_application_code_related']), ]


class LoanApplicationSpouseProfile(models.Model):
    loan_application_spouse_profile_id = models.UUIDField(
        primary_key=True, default=RandomUUID, editable=False, unique=True)
    loan_application_spouse_profile_user_related = models.CharField(max_length=255, null=False, editable=False)
    loan_application_spouse_profile_code_related = models.CharField(max_length=255, null=False, editable=False)
    loan_application_spouse_profile_guarantor = models.BooleanField(null=False, editable=False)
    loan_application_spouse_profile_full_name = models.CharField(max_length=255, null=False, editable=False)
    loan_application_spouse_profile_status = models.CharField(max_length=255, null=False, editable=False)
    loan_application_spouse_profile_dob = models.DateField(null=False, editable=False)
    loan_application_spouse_profile_pob = models.CharField(max_length=255, null=False, editable=False)
    loan_application_spouse_profile_address = models.TextField(null=False, editable=False)
    loan_application_spouse_profile_province = models.CharField(max_length=255, null=False, editable=False)
    loan_application_spouse_profile_district = models.CharField(max_length=255, null=False, editable=False)
    loan_application_spouse_profile_sub_district = models.CharField(max_length=255, null=False, editable=False)
    loan_application_spouse_profile_postal_code = models.CharField(max_length=255, null=False, editable=False)
    loan_application_spouse_profile_phone_number = models.CharField(max_length=20, null=False, editable=False)
    loan_application_spouse_profile_join_income = models.BooleanField(null=False, editable=False, default=False)
    loan_application_spouse_profile_company_name = models.CharField(max_length=255, null=True)
    loan_application_spouse_profile_company_phone = models.CharField(max_length=255, null=True)
    loan_application_spouse_profile_company_address_prov = models.CharField(max_length=255, null=True)
    loan_application_spouse_profile_company_address_district = models.CharField(max_length=255, null=True)
    loan_application_spouse_profile_company_address_sub_district = models.CharField(max_length=255, null=True)
    loan_application_spouse_profile_company_address = models.TextField(null=True)
    loan_application_spouse_profile_company_postal_code = models.CharField(max_length=5, null=True)
    loan_application_spouse_profile_company_establish_from = models.DateField(editable=False, null=True)
    loan_application_spouse_profile_company_category = models.CharField(max_length=255, null=True)
    loan_application_spouse_profile_job_started_date = models.DateField(editable=False, null=True)
    loan_application_spouse_profile_job_status = models.CharField(max_length=255, null=True)
    loan_application_spouse_profile_job_evident = models.TextField(null=True)
    loan_application_spouse_profile_salary = models.DecimalField(
        editable=False, null=False, max_digits=30, decimal_places=12, default=0)
    loan_application_spouse_profile_placement = models.CharField(max_length=255, null=True)
    loan_application_spouse_profile_selfie = models.TextField(null=True)
    loan_application_spouse_profile_selfie_eidentity = models.TextField(null=True)
    loan_application_spouse_profile_eidentity = models.TextField(null=True)
    loan_application_spouse_profile_enpwp = models.TextField(null=True)
    loan_application_spouse_profile_family_card = models.TextField(null=True)
    loan_application_spouse_marriage_certificate = models.TextField(null=True)
    loan_application_spouse_profile_created_by = models.CharField(max_length=255, null=False)
    loan_application_spouse_profile_created_date = models.DateTimeField(
        editable=False, null=False, auto_now_add=True)
    loan_application_spouse_profile_created_by_job = models.CharField(max_length=255, null=False)
    loan_application_spouse_profile_created_date_job = models.DateTimeField(
        editable=False, null=False, auto_now_add=True)
    loan_application_spouse_profile_created_by_selfie = models.CharField(max_length=255, null=False)
    loan_application_spouse_profile_created_date_selfie = models.DateTimeField(
        editable=False)

    def __str__(self):
        return self.loan_application_spouse_profile_user_related

    def __unicode__(self):
        return '%s' % self.loan_application_spouse_profile_user_related

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.loan_application_spouse_profile_id),
            escape(self.loan_application_spouse_profile_user_related),
            escape(self.loan_application_spouse_profile_code_related),
            escape(self.loan_application_spouse_profile_guarantor),
            escape(self.loan_application_spouse_profile_full_name),
            escape(self.loan_application_spouse_profile_status), escape(self.loan_application_spouse_profile_dob),
            escape(self.loan_application_spouse_profile_pob), escape(self.loan_application_spouse_profile_address),
            escape(self.loan_application_spouse_profile_province),
            escape(self.loan_application_spouse_profile_district),
            escape(self.loan_application_spouse_profile_sub_district),
            escape(self.loan_application_spouse_profile_postal_code),
            escape(self.loan_application_spouse_profile_phone_number),
            escape(self.loan_application_spouse_profile_join_income),
            escape(self.loan_application_spouse_profile_company_name),
            escape(self.loan_application_spouse_profile_company_phone),
            escape(self.loan_application_spouse_profile_company_address_prov),
            escape(self.loan_application_spouse_profile_company_address_district),
            escape(self.loan_application_spouse_profile_company_address_sub_district),
            escape(self.loan_application_spouse_profile_company_address),
            escape(self.loan_application_spouse_profile_company_postal_code),
            escape(self.loan_application_spouse_profile_company_establish_from),
            escape(self.loan_application_spouse_profile_company_category),
            escape(self.loan_application_spouse_profile_job_started_date),
            escape(self.loan_application_spouse_profile_job_status),
            escape(self.loan_application_spouse_profile_job_evident),
            escape(self.loan_application_spouse_profile_salary),
            escape(self.loan_application_spouse_profile_placement),
            escape(self.loan_application_spouse_profile_selfie),
            escape(self.loan_application_spouse_profile_selfie_eidentity),
            escape(self.loan_application_spouse_profile_eidentity),
            escape(self.loan_application_spouse_profile_enpwp),
            escape(self.loan_application_spouse_profile_family_card),
            escape(self.loan_application_spouse_marriage_certificate),
            escape(self.loan_application_spouse_profile_created_by),
            escape(self.loan_application_spouse_profile_created_date),
            escape(self.loan_application_spouse_profile_created_by_job),
            escape(self.loan_application_spouse_profile_created_date_job),
            escape(self.loan_application_spouse_profile_created_by_selfie),
            escape(self.loan_application_spouse_profile_created_date_selfie),
        )

    class Meta:
        ordering = ('loan_application_spouse_profile_id',)
        indexes = [
            models.Index(
                fields=['loan_application_spouse_profile_id',
                        'loan_application_spouse_profile_user_related',
                        'loan_application_spouse_profile_code_related']), ]


class LoanCurrentJobs(models.Model):
    loan_current_jobs_id = models.UUIDField(
        primary_key=True, default=RandomUUID, editable=False, unique=True)
    loan_current_jobs_user_related = models.CharField(max_length=255, null=False)
    loan_current_jobs_code_related = models.CharField(max_length=255, null=False, editable=False)
    loan_current_jobs_company_name = models.CharField(max_length=255, null=False)
    loan_current_jobs_company_phone = models.CharField(max_length=255, null=False)
    loan_current_jobs_company_address_prov = models.CharField(max_length=255, null=True)
    loan_current_jobs_company_address_district = models.CharField(max_length=255, null=True)
    loan_current_jobs_company_address_sub_district = models.CharField(max_length=255, null=True)
    loan_current_jobs_company_address = models.TextField(null=False)
    loan_current_jobs_company_postal_code = models.CharField(max_length=5, null=True)
    loan_current_jobs_company_establish_from = models.DateField(editable=False, null=False)
    loan_current_jobs_company_category = models.CharField(max_length=255, null=True)
    loan_current_jobs_started_date = models.DateField(editable=False, null=False)
    loan_current_jobs_status = models.CharField(max_length=255, null=False)
    loan_current_jobs_salary = models.DecimalField(
        editable=False, null=False, max_digits=30, decimal_places=12, default=0)
    loan_current_jobs_placement = models.CharField(max_length=255, null=False)
    loan_current_jobs_evident = models.TextField(null=True)
    loan_current_jobs_created_by = models.CharField(max_length=255, null=False)
    loan_current_jobs_created_date = models.DateTimeField(editable=False, null=False, auto_now_add=True)

    def __str__(self):
        return self.loan_current_jobs_user_related

    def __unicode__(self):
        return '%s' % self.loan_current_jobs_user_related

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.loan_current_jobs_id), escape(self.loan_current_jobs_user_related),
            escape(self.loan_current_jobs_code_related),
            escape(self.loan_current_jobs_company_name), escape(self.loan_current_jobs_company_phone),
            escape(self.loan_current_jobs_company_address_prov),
            escape(self.loan_current_jobs_company_address_district),
            escape(self.loan_current_jobs_company_address_sub_district), escape(self.loan_current_jobs_company_address),
            escape(self.loan_current_jobs_company_establish_from), escape(self.loan_current_jobs_company_category),
            escape(self.loan_current_jobs_started_date), escape(self.loan_current_jobs_status),
            escape(self.loan_current_jobs_salary), escape(self.loan_current_jobs_placement),
            escape(self.loan_current_jobs_evident),
            escape(self.loan_current_jobs_created_by), escape(self.loan_current_jobs_created_date)
        )

    class Meta:
        ordering = ('loan_current_jobs_id',)
        indexes = [
            models.Index(
                fields=['loan_current_jobs_id',
                        'loan_current_jobs_user_related',
                        'loan_current_jobs_code_related']), ]


class LoanApplicationVerification(models.Model):
    loan_application_verification_id = models.UUIDField(
        primary_key=True, default=RandomUUID, editable=False, unique=True)
    loan_application_verification_user_related = models.CharField(max_length=255, null=False, editable=False)
    loan_application_verification_related_loan = models.CharField(max_length=255, null=False, editable=False)
    loan_application_verification_user_jobs_company_name = models.BooleanField(null=False, editable=False, default=False)
    loan_application_verification_user_jobs_company_address = models.BooleanField(null=False, editable=False, default=False)
    loan_application_verification_user_jobs_company_phone = models.BooleanField(null=False, editable=False, default=False)
    loan_application_verification_user_jobs_company_establish = models.BooleanField(null=False, editable=False, default=False)
    loan_application_verification_user_jobs_salary = models.BooleanField(null=False, editable=False, default=False)
    loan_application_verification_user_jobs_true_salary = models.DecimalField(
        editable=False, null=False, max_digits=30, decimal_places=12, default=0)
    loan_application_verification_user_jobs_placement = models.BooleanField(null=False, editable=False, default=False)
    loan_application_verification_user_jobs_status = models.BooleanField(null=False, editable=False, default=False)
    loan_application_verification_user_jobs_true_status = models.CharField(max_length=255, null=False, default=0)
    loan_application_verification_user_jobs_start_date = models.DateField(null=True)
    loan_application_verification_user_jobs_true_start_date = models.DateField(editable=False, null=True)
    loan_application_verification_spouse_ekyc_score = models.DecimalField(
        editable=False, null=False, max_digits=5, decimal_places=2, default=0)
    loan_application_verification_spouse_jobs_company_name = models.BooleanField(null=True)
    loan_application_verification_spouse_jobs_company_address = models.BooleanField(null=True)
    loan_application_verification_spouse_jobs_company_phone = models.BooleanField(null=True)
    loan_application_verification_spouse_jobs_company_establish = models.BooleanField(null=True)
    loan_application_verification_spouse_jobs_salary = models.BooleanField(null=True)
    loan_application_verification_spouse_jobs_true_salary = models.DecimalField(
        editable=False, null=True, max_digits=30, decimal_places=12, default=0)
    loan_application_verification_spouse_jobs_placement = models.BooleanField(null=True)
    loan_application_verification_spouse_jobs_status = models.BooleanField(null=True)
    loan_application_verification_spouse_jobs_true_status = models.CharField(max_length=255, null=True)
    loan_application_verification_spouse_jobs_start_date = models.BooleanField(null=True)
    loan_application_verification_spouse_jobs_true_start_date = models.DateField(editable=False, null=True)
    loan_application_verification_document_number = models.CharField(max_length=255, null=True)
    loan_application_verification_document_pic = models.TextField(null=False)
    loan_application_verification_created_by = models.CharField(max_length=255, null=False)
    loan_application_verification_created_date = models.DateTimeField(editable=False, null=False, auto_now_add=True)

    def __str__(self):
        return self.loan_application_verification_user_related

    def __unicode__(self):
        return '%s' % self.loan_application_verification_user_related

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.loan_application_verification_id), escape(self.loan_application_verification_user_related),
            escape(self.loan_application_verification_related_loan),
            escape(self.loan_application_verification_user_jobs_company_name),
            escape(self.loan_application_verification_user_jobs_company_address),
            escape(self.loan_application_verification_user_jobs_company_phone),
            escape(self.loan_application_verification_user_jobs_company_establish),
            escape(self.loan_application_verification_user_jobs_salary),
            escape(self.loan_application_verification_user_jobs_true_salary),
            escape(self.loan_application_verification_user_jobs_placement),
            escape(self.loan_application_verification_user_jobs_status),
            escape(self.loan_application_verification_user_jobs_true_status),
            escape(self.loan_application_verification_user_jobs_start_date),
            escape(self.loan_application_verification_user_jobs_true_start_date),
            escape(self.loan_application_verification_spouse_ekyc_score),
            escape(self.loan_application_verification_spouse_jobs_company_name),
            escape(self.loan_application_verification_spouse_jobs_company_address),
            escape(self.loan_application_verification_spouse_jobs_company_phone),
            escape(self.loan_application_verification_spouse_jobs_company_establish),
            escape(self.loan_application_verification_spouse_jobs_salary),
            escape(self.loan_application_verification_spouse_jobs_true_salary),
            escape(self.loan_application_verification_spouse_jobs_placement),
            escape(self.loan_application_verification_spouse_jobs_status),
            escape(self.loan_application_verification_spouse_jobs_true_status),
            escape(self.loan_application_verification_spouse_jobs_start_date),
            escape(self.loan_application_verification_spouse_jobs_true_start_date),
            escape(self.loan_application_verification_document_number),
            escape(self.loan_application_verification_document_pic),
            escape(self.loan_application_verification_created_by),
            escape(self.loan_application_verification_created_date),
        )

    class Meta:
        ordering = ('loan_application_verification_id',)
        indexes = [
            models.Index(
                fields=['loan_application_verification_id',
                        'loan_application_verification_user_related',
                        'loan_application_verification_related_loan']), ]


class LoanAppraisalCollateral(models.Model):
    loan_appraisal_collateral_id = models.UUIDField(
        primary_key=True, default=RandomUUID, editable=False, unique=True)
    loan_appraisal_collateral_user_related = models.CharField(max_length=255, null=False, editable=False)
    loan_appraisal_collateral_related_loan = models.CharField(max_length=255, null=False, editable=False)
    loan_appraisal_collateral_status = models.CharField(max_length=255, null=False, editable=False)
    loan_appraisal_collateral_value = models.DecimalField(
        editable=False, null=False, max_digits=5, decimal_places=2, default=0)
    loan_appraisal_collateral_picture = models.TextField(null=False)
    loan_appraisal_collateral_document_number = models.CharField(max_length=255, null=False, editable=False)
    loan_appraisal_collateral_document_pic = models.TextField(null=False)
    loan_appraisal_collateral_created_by = models.CharField(max_length=255, null=False)
    loan_appraisal_collateral_created_date = models.DateTimeField(editable=False, null=False, auto_now_add=True)

    def __str__(self):
        return self.loan_appraisal_collateral_user_related

    def __unicode__(self):
        return '%s' % self.loan_appraisal_collateral_user_related

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.loan_appraisal_collateral_id), escape(self.loan_appraisal_collateral_user_related),
            escape(self.loan_appraisal_collateral_status), escape(self.loan_appraisal_collateral_value),
            escape(self.loan_appraisal_collateral_picture), escape(self.loan_appraisal_collateral_document_number),
            escape(self.loan_appraisal_collateral_document_pic),
            escape(self.loan_appraisal_collateral_created_by), escape(self.loan_appraisal_collateral_created_date),
        )

    class Meta:
        ordering = ('loan_appraisal_collateral_id',)
        indexes = [
            models.Index(
                fields=['loan_appraisal_collateral_id',
                        'loan_appraisal_collateral_user_related']), ]


class LoanMarginConfigurable(models.Model):
    loan_margin_configurable_id = models.UUIDField(
        primary_key=True, default=RandomUUID, editable=False, unique=True)
    loan_margin_configurable_default_name = models.CharField(max_length=255, null=False, editable=False)
    loan_margin_configurable_default_margin = models.DecimalField(
        editable=False, null=False, max_digits=7, decimal_places=4, default=0)
    loan_margin_configurable_created_by = models.CharField(max_length=255, null=False, editable=False)
    loan_margin_configurable_created_date = models.DateTimeField(editable=False, null=False, auto_now_add=True)

    def __str__(self):
        return self.loan_margin_configurable_default_name

    def __unicode__(self):
        return '%s' % self.loan_margin_configurable_default_name

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.loan_margin_configurable_id), escape(self.loan_margin_configurable_default_name),
            escape(self.loan_margin_configurable_default_margin),
            escape(self.loan_margin_configurable_created_by), escape(self.loan_margin_configurable_created_date),
        )

    class Meta:
        ordering = ('loan_margin_configurable_id',)
        indexes = [
            models.Index(
                fields=['loan_margin_configurable_id']), ]


class LoanApproval(models.Model):
    loan_approval_id = models.UUIDField(
        primary_key=True, default=RandomUUID, editable=False, unique=True)
    loan_approval_user_related = models.CharField(max_length=255, null=False, editable=False)
    loan_approval_related_loan = models.CharField(max_length=255, null=False, editable=False)
    loan_approval_status = models.CharField(max_length=255, null=False, editable=False, default='On Manual Verify')
    loan_approval_comment = models.TextField(null=False, editable=False, default=0)
    loan_approval_amount = models.DecimalField(
        editable=False, null=False, max_digits=30, decimal_places=12, default=0)
    loan_approval_installment_month = models.DecimalField(
        editable=False, null=False, max_digits=3, decimal_places=0, default=0)
    loan_approval_installment_amount = models.DecimalField(
        editable=False, null=False, max_digits=30, decimal_places=12, default=0)
    loan_approval_current_amount = models.DecimalField(
        editable=False, null=False, max_digits=30, decimal_places=12, default=0)
    loan_approval_raised_fund = models.BooleanField(null=True, editable=False)
    loan_approval_auto_debit_date = models.DateField(null=True, editable=False)
    loan_approval_use_insurance = models.BooleanField(null=True, editable=False)
    loan_approval_insurance_code = models.CharField(max_length=255, null=True, editable=False)
    loan_approval_margin_related = models.CharField(max_length=255, null=True, editable=False)
    loan_approval_finish_status = models.BooleanField(null=True, editable=False)
    loan_approval_created_by = models.CharField(max_length=255, null=True, editable=False)
    loan_approval_created_date = models.DateTimeField(editable=False, null=False, auto_now_add=True)

    def __str__(self):
        return self.loan_approval_user_related

    def __unicode__(self):
        return '%s' % self.loan_approval_user_related

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.loan_approval_id), escape(self.loan_approval_user_related),
            escape(self.loan_approval_related_loan), escape(self.loan_approval_status),
            escape(self.loan_approval_comment), escape(self.loan_approval_amount),
            escape(self.loan_approval_installment_month), escape(self.loan_approval_installment_amount),
            escape(self.loan_approval_current_amount), escape(self.loan_approval_raised_fund),
            escape(self.loan_approval_use_insurance), escape(self.loan_approval_insurance_code),
            escape(self.loan_approval_margin_related), escape(self.loan_approval_finish_status),
            escape(self.loan_approval_created_by), escape(self.loan_approval_created_date),
        )

    class Meta:
        ordering = ('loan_approval_id',)
        indexes = [
            models.Index(
                fields=['loan_approval_id',
                        'loan_approval_user_related',
                        'loan_approval_related_loan']), ]