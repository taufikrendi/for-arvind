from django.utils import timezone
from django.contrib.postgres.functions import RandomUUID

from django.db import models


class DepositMemberPrincipal(models.Model):
    deposit_member_principal_id = models.UUIDField(
        primary_key=True, default=RandomUUID, editable=False, unique=True)
    deposit_member_principal_user_related = models.CharField(max_length=255, null=False, editable=False)
    deposit_member_principal_payment_principal_status = models.BooleanField(editable=False, null=False, default=False)
    deposit_member_principal_payment_principal_amount = models.DecimalField(
        editable=False, null=False, max_digits=30, decimal_places=12, default=0)
    deposit_member_principal_payment_transaction_number = models.CharField(
        max_length=255, editable=False, unique=True)
    deposit_member_principal_created_by = models.CharField(max_length=255, null=False, editable=False)
    deposit_member_principal_created_date = models.DateTimeField(
        editable=False, null=False, auto_now_add=True)

    def __str__(self):
        return self.deposit_member_principal_user_related

    def __unicode__(self):
        return '%s' % self.deposit_member_principal_user_related

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.deposit_member_principal_id), escape(self.deposit_member_principal_user_related),
            escape(self.deposit_member_principal_payment_principal_status),
            escape(self.deposit_member_principal_payment_principal_amount),
            escape(self.deposit_member_principal_payment_transaction_number),
            escape(self.deposit_member_principal_created_by), escape(self.deposit_member_principal_created_date),
        )

    class Meta:
        ordering = ('-deposit_member_principal_user_related',)
        indexes = [
            models.Index(
                fields=[
                    'deposit_member_principal_id',
                    'deposit_member_principal_user_related']), ]


class DepositMemberMandatory(models.Model):
    deposit_member_mandatory_id = models.UUIDField(
        primary_key=True, default=RandomUUID, editable=False, unique=True)
    deposit_member_mandatory_user_related = models.CharField(max_length=255, null=False, editable=False)
    deposit_member_mandatory_amount = models.DecimalField(
        editable=False, null=False, max_digits=30, decimal_places=12, default=0)
    deposit_member_mandatory_period_left = models.IntegerField(editable=False, null=False, default=0)
    deposit_member_mandatory_period_end = models.DateTimeField(
        editable=False, null=True)
    deposit_member_mandatory_created_by = models.CharField(max_length=255, null=False, editable=False)
    deposit_member_mandatory_created_date = models.DateTimeField(
        editable=False, null=False, auto_now_add=True)
    deposit_member_mandatory_updated_by = models.CharField(max_length=255, null=False, editable=False)
    deposit_member_mandatory_updated_date = models.DateTimeField(
        editable=False, null=True)

    def __str__(self):
        return self.deposit_member_mandatory_user_related

    def __unicode__(self):
        return '%s' % self.deposit_member_mandatory_user_related

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.deposit_member_mandatory_id), escape(self.deposit_member_mandatory_user_related),
            escape(self.deposit_member_mandatory_amount), escape(self.deposit_member_mandatory_period_left),
            escape(self.deposit_member_mandatory_period_end),
            escape(self.deposit_member_mandatory_created_by), escape(self.deposit_member_mandatory_created_date),
            escape(self.deposit_member_mandatory_updated_by), escape(self.deposit_member_mandatory_updated_date),
        )

    class Meta:
        ordering = ('-deposit_member_mandatory_user_related',)
        indexes = [
            models.Index(
                fields=['deposit_member_mandatory_id',
                        'deposit_member_mandatory_user_related']), ]


class DepositProductMaster(models.Model):
    deposit_product_master_id = models.UUIDField(
        primary_key=True, default=RandomUUID, editable=False, unique=True)
    deposit_product_master_name = models.CharField(max_length=255, null=False, editable=False)
    deposit_product_master_description = models.TextField(null=False, editable=False)
    deposit_product_active = models.BooleanField(null=False, default=False)
    deposit_product_master_revenue_share = models.DecimalField(
        editable=False, null=False, max_digits=6, decimal_places=4)
    deposit_product_minimum_amount = models.DecimalField(
        editable=False, null=False, max_digits=30, decimal_places=12, default=0)
    deposit_product_minimum_fluctuate_revenue = models.BooleanField(null=False, default=False)
    deposit_product_master_created_by = models.CharField(max_length=255, null=False, editable=False)
    deposit_product_master_created_date = models.DateTimeField(
        editable=False, null=False, auto_now_add=True)

    def __str__(self):
        return self.deposit_product_master_name

    def __unicode__(self):
        return '%s' % self.deposit_product_master_name

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.deposit_product_master_id),
            escape(self.deposit_product_master_name),
            escape(self.deposit_product_master_description),
            escape(self.deposit_product_active),
            escape(self.deposit_product_master_revenue_share),
            escape(self.deposit_product_minimum_amount),
            escape(self.deposit_product_minimum_fluctuate_revenue),
            escape(self.deposit_product_master_created_by),
            escape(self.deposit_product_master_created_date),
        )
    class Meta:
        ordering = ('-deposit_product_master_created_date',)
        indexes = [
            models.Index(
                fields=['deposit_product_master_id', ]), ]


class DepositMemberCurrent(models.Model):
    deposit_member_current_id = models.UUIDField(
        primary_key=True, default=RandomUUID, editable=False, unique=True)
    deposit_member_current_user_related = models.CharField(max_length=255, null=False, editable=False)
    deposit_member_current_transaction_related = models.CharField(max_length=255, null=False, editable=False)
    deposit_member_current_amount = models.DecimalField(
        editable=False, null=False, max_digits=30, decimal_places=12, default=0)
    deposit_member_current_total_profit_share = models.DecimalField(
        editable=False, null=False, max_digits=30, decimal_places=12, default=0)
    deposit_member_current_period_base = models.IntegerField(editable=False, null=False, default=0)
    deposit_member_current_period_left = models.IntegerField(editable=False, null=False, default=0)
    deposit_member_current_finished_status = models.BooleanField(null=False)
    deposit_member_current_created_by = models.CharField(max_length=255, null=False, editable=False)
    deposit_member_current_created_date = models.DateTimeField(
        editable=False, null=False, auto_now_add=True)

    def __str__(self):
        return self.deposit_member_current_user_related

    def __unicode__(self):
        return '%s' % self.deposit_member_current_user_related

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.deposit_member_current_id), escape(self.deposit_member_current_user_related),
            escape(self.deposit_member_current_transaction_related),
            escape(self.deposit_member_current_amount),
            escape(self.deposit_member_current_total_profit_share),
            escape(self.deposit_member_current_period_base),
            escape(self.deposit_member_current_period_left),
            escape(self.deposit_member_current_finished_status),
            escape(self.deposit_member_current_created_by),
            escape(self.deposit_member_current_created_date),
        )

    class Meta:
        ordering = ('-deposit_member_current_id',)
        indexes = [
            models.Index(
                fields=['deposit_member_current_id',
                        'deposit_member_current_user_related',
                        'deposit_member_current_transaction_related']), ]
