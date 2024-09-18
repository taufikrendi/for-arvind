from django.utils import timezone
from django.contrib.postgres.functions import RandomUUID
from django.db import models


class TransactionDepositTransit(models.Model):
    transaction_deposit_transit_id = models.UUIDField(
        primary_key=True, default=RandomUUID, editable=False, unique=True)
    transaction_deposit_transit_user_related = models.CharField(max_length=255, null=False, editable=False)
    transaction_deposit_transit_code = models.CharField(
        max_length=255, editable=False, unique=True)
    transaction_deposit_transit_amount = models.DecimalField(
        editable=False, max_digits=30, decimal_places=12, null=True)
    transaction_deposit_transit_unique_code_amount = models.DecimalField(
        editable=False, max_digits=30, decimal_places=12, null=True)
    transaction_deposit_transit_gt_amount = models.DecimalField(
        editable=False, max_digits=30, decimal_places=12, null=True)
    transaction_deposit_transit_type = models.CharField(
        max_length=13, editable=False, null=False)
    transaction_deposit_transit_created_by = models.CharField(max_length=255, null=False, editable=False)
    transaction_deposit_transit_created_date = models.DateTimeField(
        editable=False, null=False, auto_now_add=True)

    def __str__(self):
        return self.transaction_deposit_transit_user_related

    def __unicode__(self):
        return '%s' % self.transaction_deposit_transit_user_related

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.transaction_deposit_transit_id), escape(self.transaction_deposit_transit_user_related),
            escape(self.transaction_deposit_transit_amount),
            escape(self.transaction_deposit_transit_unique_code_amount),
            escape(self.transaction_deposit_transit_gt_amount), escape(self.transaction_deposit_transit_type),
            escape(self.transaction_deposit_transit_created_by), escape(self.transaction_deposit_transit_created_date)
        )

    class Meta:
        ordering = ('transaction_deposit_transit_id',)
        indexes = [
            models.Index(
                fields=['transaction_deposit_transit_id',
                        'transaction_deposit_transit_user_related']), ]


class TransactionDepositVerified(models.Model):
    transaction_deposit_verified_id = models.UUIDField(
        primary_key=True, default=RandomUUID, editable=False, unique=True)
    transaction_deposit_verified_user_related = models.CharField(max_length=255, null=False, editable=False)
    transaction_deposit_verified_transit_code = models.CharField(
        max_length=255, editable=False, unique=True)
    transaction_deposit_verified_status = models.CharField(max_length=255, null=False, editable=False)
    transaction_deposit_verified_image_proof = models.TextField(null=True)
    transaction_deposit_verified_image_proof_status = models.BooleanField(default=False)
    transaction_deposit_verified_approval_status = models.BooleanField(default=False)
    transaction_deposit_verified_created_by = models.CharField(max_length=255, null=False, editable=False)
    transaction_deposit_verified_created_date = models.DateTimeField(
        editable=False, null=True, auto_now_add=True)
    transaction_deposit_verified_created_by_admin = models.CharField(max_length=255, null=True, editable=False)
    transaction_deposit_verified_created_date_admin = models.DateTimeField(
        editable=False, null=True)

    def __str__(self):
        return self.transaction_deposit_verified_user_related

    def __unicode__(self):
        return '%s' % self.transaction_deposit_verified_user_related

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.transaction_deposit_verified_id), escape(self.transaction_deposit_verified_user_related),
            escape(self.transaction_deposit_verified_transit_code),
            escape(self.transaction_deposit_verified_status), escape(self.transaction_deposit_verified_image_proof),
            escape(self.transaction_deposit_verified_image_proof_status),
            escape(self.transaction_deposit_verified_approval_status),
            escape(self.transaction_deposit_verified_created_by),
            escape(self.transaction_deposit_verified_created_date),
            escape(self.transaction_deposit_verified_created_by_admin),
            escape(self.transaction_deposit_verified_created_date_admin),
        )

    class Meta:
        ordering = ('-transaction_deposit_verified_id',)
        indexes = [
            models.Index(
                fields=['transaction_deposit_verified_id',
                        'transaction_deposit_verified_user_related',
                        'transaction_deposit_verified_transit_code']), ]


class TransactionDepositTimeTransit(models.Model):
    transaction_deposit_time_transit_id = models.UUIDField(
        primary_key=True, default=RandomUUID, editable=False, unique=True)
    transaction_deposit_time_transit_user_related = models.CharField(max_length=255, null=False, editable=False)
    transaction_deposit_time_transit_code = models.CharField(
        max_length=255, editable=False, unique=True, null=False)
    transaction_deposit_time_transit_product_type = models.CharField(max_length=255, null=False, editable=False)
    transaction_deposit_time_transit_amount = models.DecimalField(
        editable=False, null=False, max_digits=30, decimal_places=12, default=0)
    transaction_deposit_time_transit_period_base = models.IntegerField(editable=False, null=False, default=0)
    transaction_deposit_time_transit_type = models.CharField(
        max_length=13, editable=False, null=False)
    transaction_deposit_time_revenue_share = models.DecimalField(
        editable=False, null=False, max_digits=6, decimal_places=4)
    transaction_deposit_time_fluctuate_revenue = models.BooleanField(null=False, default=False)
    transaction_deposit_time_transit_created_by = models.CharField(max_length=255, null=False, editable=False)
    transaction_deposit_time_transit_created_date = models.DateTimeField(
        editable=False, null=False, auto_now_add=True)

    def __str__(self):
        return self.transaction_deposit_time_transit_user_related

    def __unicode__(self):
        return '%s' % self.transaction_deposit_time_transit_user_related

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.transaction_deposit_time_transit_id),
            escape(self.transaction_deposit_time_transit_user_related),
            escape(self.transaction_deposit_time_transit_code),
            escape(self.transaction_deposit_time_transit_product_type),
            escape(self.transaction_deposit_time_transit_amount),
            escape(self.transaction_deposit_time_transit_period_base),
            escape(self.transaction_deposit_time_transit_type),
            escape(self.transaction_deposit_time_revenue_share),
            escape(self.transaction_deposit_time_fluctuate_revenue),
            escape(self.transaction_deposit_time_transit_created_by),
            escape(self.transaction_deposit_time_transit_created_date),
        )

    class Meta:
        ordering = ('-transaction_deposit_time_transit_id',)
        indexes = [
            models.Index(
                fields=['transaction_deposit_time_transit_id',
                        'transaction_deposit_time_transit_user_related',
                        'transaction_deposit_time_transit_code']), ]