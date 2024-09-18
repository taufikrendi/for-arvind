from django.utils import timezone
from django.contrib.postgres.functions import RandomUUID
from django.db import models

from utils.validators import numeric


# Create your models here.
class AccountProfile(models.Model):
    account_profile_id = models.UUIDField(
        primary_key=True, default=RandomUUID, editable=False, unique=True)
    account_profile_user_related = models.CharField(max_length=255, null=False, editable=False)
    account_profile_phone_number = models.CharField(max_length=15, null=False)
    account_profile_identification_number = models.CharField(
        max_length=16, unique=True, default=None, null=True)
    account_profile_tax_identification_number = models.CharField(
        max_length=15, unique=True, default=None, null=True)
    account_profile_dob = models.DateField(null=True)
    account_profile_sex = models.CharField(max_length=6, null=True)
    account_profile_address = models.TextField(max_length=500, null=True)
    account_profile_pob = models.CharField(max_length=255, null=True)
    account_profile_address_prov = models.CharField(max_length=255, null=True)
    account_profile_address_district = models.CharField(max_length=255, null=True)
    account_profile_address_sub_district = models.CharField(max_length=255, null=True)
    account_profile_selfie = models.TextField(null=True)
    account_profile_selfie_eidentity = models.TextField(null=True)
    account_profile_eidentity = models.TextField(null=True)
    account_profile_enpwp = models.TextField(null=True)
    account_profile_cif_number = models.IntegerField(null=True, unique=True)
    account_profile_cooperative_number = models.CharField(max_length=255, null=True)
    account_profile_filled_status = models.BooleanField(default=False)
    account_profile_created_by = models.CharField(max_length=255, null=False, editable=False)
    account_profile_created_date = models.DateTimeField(
        editable=False, null=False, blank=True, auto_now_add=True)
    account_profile_updated_by = models.CharField(max_length=255, null=True)
    account_profile_updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.account_profile_user_related

    #
    def __unicode__(self):
        return '%s' % self.account_profile_user_related

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.account_profile_id), escape(self.account_profile_user_related),
            escape(self.account_profile_phone_number), escape(self.account_profile_tax_identification_number),
            escape(self.account_profile_identification_number), escape(self.account_profile_dob),
            escape(self.account_profile_pob), escape(self.account_profile_address),
            escape(self.account_profile_address_prov), escape(self.account_profile_address_district),
            escape(self.account_profile_address_sub_district), escape(self.account_profile_created_date),
            escape(self.account_profile_created_by), escape(self.account_profile_updated_at),
            escape(self.account_profile_updated_by), escape(self.account_profile_sex),
            escape(self.account_profile_selfie), escape(self.account_profile_selfie_eidentity),
            escape(self.account_profile_eidentity), escape(self.account_profile_enpwp),
            escape(self.account_profile_cif_number), escape(self.account_profile_cooperative_number),
            escape(self.account_profile_filled_status)
        )

    class Meta:
        ordering = ('account_profile_id',)
        indexes = [models.Index(
            fields=['account_profile_id',
                    'account_profile_user_related',
                    'account_profile_cif_number',
                    'account_profile_cooperative_number']),]


class AccountBankUsers(models.Model):
    account_bank_user_id = models.UUIDField(
        primary_key=True, default=RandomUUID, editable=False, unique=True)
    account_bank_user_name = models.CharField(max_length=50, null=True)
    account_bank_user_number = models.CharField(max_length=20, null=True, validators=[numeric])
    account_bank_user_related_to_bank = models.CharField(max_length=255, null=True)
    account_bank_user_related_to_user = models.CharField(max_length=255, null=False)
    account_bank_user_created_by = models.CharField(max_length=255, null=False)
    account_bank_user_created_date = models.DateTimeField(
        editable=False, null=False, auto_now_add=True)
    account_bank_user_updated_by = models.CharField(max_length=255, null=True)
    account_bank_user_updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '%s' % self.account_bank_user_related_to_user

    def __unicode__(self):
        return '%s' % self.account_bank_user_related_to_user

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.account_bank_user_id), escape(self.account_bank_user_name),
            escape(self.account_bank_user_number), escape(self.account_bank_user_related_to_bank),
            escape(self.account_bank_user_related_to_user),
            escape(self.account_bank_user_created_by), escape(self.account_bank_user_created_date),
            escape(self.account_bank_user_updated_by), escape(self.account_bank_user_updated_at)
        )

    class Meta:
        ordering = ('account_bank_user_id',)
        indexes = [
            models.Index(
                fields=['account_bank_user_id',
                        'account_bank_user_related_to_bank',
                        'account_bank_user_related_to_user']), ]


class AccountReplicationProfile(models.Model):
    account_replication_profile_id = models.UUIDField(
        primary_key=True, default=RandomUUID, editable=False, unique=True)
    account_replication_profile_user_related = models.CharField(max_length=255, null=False)
    account_replication_profile_phone_number = models.CharField(max_length=15, null=False, default=0, blank=False)
    account_replication_profile_identification_number = models.CharField(
        max_length=16, default=None, null=True)
    account_replication_profile_tax_identification_number = models.CharField(
        max_length=15, default=None, null=True)
    account_replication_profile_dob = models.DateField(null=True, blank=True)
    account_replication_profile_sex = models.CharField(max_length=6, null=True)
    account_replication_profile_address = models.TextField(max_length=500, null=True)
    account_replication_profile_pob = models.CharField(max_length=255, editable=False, null=False)
    account_replication_profile_address_prov = models.CharField(max_length=255, editable=False, null=False)
    account_replication_profile_address_district = models.CharField(max_length=255, editable=False, null=False)
    account_replication_profile_address_sub_district = models.CharField(max_length=255, editable=False, null=False)
    account_replication_profile_selfie = models.TextField(null=True)
    account_replication_profile_selfie_eidentity = models.TextField(null=True)
    account_replication_profile_eidentity = models.TextField(null=True)
    account_replication_profile_enpwp = models.TextField(null=True)
    account_replication_profile_cif_number = models.IntegerField(null=True, editable=False, unique=True)
    account_replication_profile_cooperative_number = models.IntegerField(null=True, editable=False, unique=True)
    account_replication_profile_filled_status = models.BooleanField(null=True, default=False)
    account_replication_profile_created_by = models.CharField(max_length=255, null=False)
    account_replication_profile_created_date = models.DateTimeField(
        editable=False, null=False, blank=True,auto_now_add=True)

    def __str__(self):
        return self.account_replication_profile_user_related

    def __unicode__(self):
        return '%s' % self.account_replication_profile_user_related

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.account_replication_profile_id), escape(self.account_replication_profile_user_related),
            escape(self.account_replication_profile_phone_number),
            escape(self.account_replication_profile_tax_identification_number),
            escape(self.account_replication_profile_identification_number),
            escape(self.account_replication_profile_dob),
            escape(self.account_replication_profile_pob), escape(self.account_replication_profile_address),
            escape(self.account_replication_profile_address_prov),
            escape(self.account_replication_profile_address_district),
            escape(self.account_replication_profile_address_sub_district),
            escape(self.account_replication_profile_created_date),
            escape(self.account_replication_profile_created_by), escape(self.account_replication_profile_sex),
            escape(self.account_replication_profile_selfie), escape(self.account_replication_profile_selfie_eidentity),
            escape(self.account_replication_profile_eidentity), escape(self.account_replication_profile_enpwp),
            escape(self.account_replication_profile_cif_number),
            escape(self.account_replication_profile_cooperative_number),
            escape(self.account_replication_profile_filled_status),
        )

    class Meta:
        ordering = ('account_replication_profile_id',)
        indexes = [models.Index(
            fields=[
                'account_replication_profile_id',
                'account_replication_profile_user_related',
                'account_replication_profile_cif_number',
                'account_replication_profile_cooperative_number']), ]


class AccountPasswordExpired(models.Model):
    account_password_expired_id = models.UUIDField(
        primary_key=True, default=RandomUUID, editable=False, unique=True)
    account_password_expired_user_related = models.CharField(max_length=255, null=False)
    account_password_expired_last_updated = models.DateTimeField(
        editable=False, null=False, auto_now_add=True)
    account_password_expired_update_by = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.account_password_expired_user_related

    def __unicode__(self):
        return '%s' % self.account_password_expired_user_related

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.account_password_expired_id), escape(self.account_password_expired_user_related),
            escape(self.account_password_expired_last_updated), escape(self.account_password_expired_update_by)
        )

    class Meta:
        ordering = ('account_password_expired_id',)
        indexes = [
            models.Index(
                fields=['account_password_expired_id',
                        'account_password_expired_user_related']), ]


class AccountMemberVerifyStatus(models.Model):
    account_member_verify_status_id = models.UUIDField(
        primary_key=True, default=RandomUUID, editable=False, unique=True)
    account_member_verify_status_user_related = models.CharField(editable=False, max_length=255, null=False)
    account_member_verify_status_user_nik = models.CharField(editable=False, max_length=255, null=True)
    account_member_verify_status_profile = models.BooleanField(editable=False, null=False, default=False)
    account_member_verify_status_profile_filled_date = models.DateTimeField(editable=False, null=True)
    account_member_verify_status_profile_close_to_update = models.BooleanField(editable=False, null=False,
                                                                               default=False)
    account_member_verify_status_dukcapil_score = models.DecimalField(max_digits=4, decimal_places=2, null=True,
                                                                      editable=False)
    account_member_verify_status_bank = models.BooleanField(editable=False, null=False, default=False)
    account_member_verify_status_bank_filled_date = models.DateTimeField(editable=False, null=True)
    account_member_verify_status_email = models.BooleanField(editable=False, null=False, default=False)
    account_member_verify_status_email_filled_date = models.DateTimeField(editable=False, null=True)
    account_member_verify_status_phone_number = models.BooleanField(editable=False, null=False, default=False)
    account_member_verify_status_phone_number_filled_date = models.DateTimeField(editable=False, null=True)
    account_member_verify_status_legal_doc_sign = models.BooleanField(editable=False, null=False, default=False)
    account_member_verify_status_legal_doc_sign_filled_date = models.DateTimeField(editable=False, null=True)
    account_member_verify_status_subscriber_agreement = models.BooleanField(editable=False, null=False, default=False)
    account_member_verify_status_subscriber_agreement_filled_date = models.DateTimeField(
        editable=False, null=False, auto_now_add=True)
    account_member_verify_status_revision_profile = models.IntegerField(editable=False, null=False, default=0)
    account_member_verify_status_revision_profile_last_date = models.DateTimeField(editable=False, null=True)
    account_member_verify_status_revision_profile_check = models.BooleanField(editable=False, null=False, default=False)
    account_member_verify_status_created_by = models.CharField(max_length=255, null=False, unique=True)
    account_member_verify_status_created_date = models.DateTimeField(
        editable=False, null=False, auto_now_add=True)
    account_member_verify_status_updated_by = models.CharField(max_length=255, null=False)
    account_member_verify_status_updated_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.account_member_verify_status_user_related

    def __unicode__(self):
        return '%s' % self.account_member_verify_status_user_related

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.account_member_verify_status_id), escape(self.account_member_verify_status_user_related),
            escape(self.account_member_verify_status_profile),
            escape(self.account_member_verify_status_profile_filled_date),
            escape(self.account_member_verify_status_bank), escape(self.account_member_verify_status_bank_filled_date),
            escape(self.account_member_verify_status_email),
            escape(self.account_member_verify_status_email_filled_date),
            escape(self.account_member_verify_status_phone_number),
            escape(self.account_member_verify_status_phone_number_filled_date),
            escape(self.account_member_verify_status_legal_doc_sign),
            escape(self.account_member_verify_status_legal_doc_sign_filled_date),
            escape(self.account_member_verify_status_subscriber_agreement),
            escape(self.account_member_verify_status_subscriber_agreement_filled_date),
            escape(self.account_member_verify_status_revision_profile),
            escape(self.account_member_verify_status_revision_profile_last_date),
            escape(self.account_member_verify_status_revision_profile_check),
            escape(self.account_member_verify_status_created_by),
            escape(self.account_member_verify_status_created_date),
            escape(self.account_member_verify_status_created_by),
            escape(self.account_member_verify_status_created_by),
            escape(self.account_member_verify_status_created_date),
            escape(self.account_member_verify_status_updated_by),
            escape(self.account_member_verify_status_updated_date),
            escape(self.account_member_verify_status_profile_close_to_update),
            escape(self.account_member_verify_status_dukcapil_score),
            escape(self.account_member_verify_status_user_nik)
        )

    class Meta:
        ordering = ('account_member_verify_status_user_related',)
        indexes = [models.Index(
            fields=[
                'account_member_verify_status_id',
                'account_member_verify_status_user_related']), ]


class AccountLogResetPassword(models.Model):
    account_log_reset_password_id = models.UUIDField(
        primary_key=True, default=RandomUUID, editable=False, unique=True)
    account_log_incoming_from = models.CharField(max_length=50, null=False, editable=False, default=None)
    account_log_reset_password_email = models.EmailField(
        max_length=255, null=False)
    account_log_reset_ip_address = models.CharField(max_length=20, null=False)
    account_log_reset_password_created_date = models.DateTimeField(editable=False, null=False, auto_now_add=True)

    def __str__(self):
        return self.account_log_reset_password_email

    def __unicode__(self):
        return '%s' % self.account_log_reset_password_email

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.account_log_reset_password_id), escape(self.account_log_reset_password_email),
            escape(self.account_log_reset_ip_address), escape(self.account_log_reset_password_user_related),
            escape(self.account_log_incoming_from), escape(self.account_log_reset_password_created_date),
        )

    class Meta:
        ordering = ('account_log_reset_password_email',)
        indexes = [models.Index(
            fields=[
                'account_log_reset_password_id',
                'account_log_reset_password_email']), ]


class AccountLogChangePassword(models.Model):
    account_log_change_password_id = models.UUIDField(
        primary_key=True, default=RandomUUID, editable=False, unique=True)
    account_log_change_password_incoming_from = models.CharField(max_length=50, null=False, editable=False,
                                                                 default=None)
    account_log_change_password_username = models.EmailField(
        max_length=255, null=False)
    account_log_change_password_ip_address = models.CharField(max_length=20, null=False)
    account_log_change_password_created_date = models.DateTimeField(editable=False, null=False, auto_now_add=True)

    def __str__(self):
        return self.account_log_change_password_username

    def __unicode__(self):
        return '%s' % self.account_log_change_password_username

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.account_log_change_password_id), escape(self.account_log_change_password_incoming_from),
            escape(self.account_log_change_password_username), escape(self.account_log_change_password_ip_address),
            escape(self.account_log_change_password_created_date)
        )

    class Meta:
        ordering = ('account_log_change_password_id',)
        indexes = [models.Index(
            fields=[
                'account_log_change_password_id',
                'account_log_change_password_username']), ]


class AccountUserPin(models.Model):
    account_user_pin_id = models.UUIDField(
        primary_key=True, default=RandomUUID, editable=False, unique=True)
    account_user_pin_related_user = models.CharField(max_length=255, null=False)
    account_user_pin_data = models.CharField(max_length=255, null=False, editable=False)
    account_user_pin_ip_address = models.CharField(max_length=20, null=False)
    account_user_pin_created_by = models.CharField(max_length=255, null=False)
    account_user_pin_created_date = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    account_user_pin_updated_by = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.account_user_pin_related_user

    def __unicode__(self):
        return '%s' % self.account_user_pin_related_user

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.account_user_pin_id), escape(self.account_user_pin_related_user),
            escape(self.account_user_pin_data), escape(self.account_user_pin_ip_address),
            escape(self.account_user_pin_created_by), escape(self.account_user_pin_created_date),
            escape(self.account_user_pin_updated_by)
        )

    class Meta:
        ordering = ('account_user_pin_related_user',)
        indexes = [models.Index(
            fields=[
                'account_user_pin_id',
                'account_user_pin_related_user']), ]

