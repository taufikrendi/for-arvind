# Generated by Django 3.1.5 on 2021-09-19 19:31

import django.contrib.postgres.functions
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountBankUsers',
            fields=[
                ('account_bank_user_id', models.UUIDField(default=django.contrib.postgres.functions.RandomUUID, editable=False, primary_key=True, serialize=False, unique=True)),
                ('account_bank_user_name', models.CharField(max_length=50, null=True)),
                ('account_bank_user_number', models.CharField(max_length=20, null=True, validators=[django.core.validators.RegexValidator('^[1-9+]', 'Only digit characters.')])),
                ('account_bank_user_related_to_bank', models.CharField(max_length=255, null=True)),
                ('account_bank_user_related_to_user', models.CharField(max_length=255)),
                ('account_bank_user_created_by', models.CharField(max_length=255)),
                ('account_bank_user_created_date', models.DateTimeField(auto_now_add=True)),
                ('account_bank_user_updated_by', models.CharField(max_length=255, null=True)),
                ('account_bank_user_updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('account_bank_user_id',),
            },
        ),
        migrations.CreateModel(
            name='AccountLogChangePassword',
            fields=[
                ('account_log_change_password_id', models.UUIDField(default=django.contrib.postgres.functions.RandomUUID, editable=False, primary_key=True, serialize=False, unique=True)),
                ('account_log_change_password_incoming_from', models.CharField(default=None, editable=False, max_length=50)),
                ('account_log_change_password_username', models.EmailField(max_length=255)),
                ('account_log_change_password_ip_address', models.CharField(max_length=20)),
                ('account_log_change_password_created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('account_log_change_password_id',),
            },
        ),
        migrations.CreateModel(
            name='AccountLogResetPassword',
            fields=[
                ('account_log_reset_password_id', models.UUIDField(default=django.contrib.postgres.functions.RandomUUID, editable=False, primary_key=True, serialize=False, unique=True)),
                ('account_log_incoming_from', models.CharField(default=None, editable=False, max_length=50)),
                ('account_log_reset_password_email', models.EmailField(max_length=255)),
                ('account_log_reset_ip_address', models.CharField(max_length=20)),
                ('account_log_reset_password_created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('account_log_reset_password_email',),
            },
        ),
        migrations.CreateModel(
            name='AccountMemberVerifyStatus',
            fields=[
                ('account_member_verify_status_id', models.UUIDField(default=django.contrib.postgres.functions.RandomUUID, editable=False, primary_key=True, serialize=False, unique=True)),
                ('account_member_verify_status_user_related', models.CharField(editable=False, max_length=255)),
                ('account_member_verify_status_user_nik', models.CharField(editable=False, max_length=255, null=True)),
                ('account_member_verify_status_profile', models.BooleanField(default=False, editable=False)),
                ('account_member_verify_status_profile_filled_date', models.DateTimeField(editable=False, null=True)),
                ('account_member_verify_status_profile_close_to_update', models.BooleanField(default=False, editable=False)),
                ('account_member_verify_status_dukcapil_score', models.DecimalField(decimal_places=2, editable=False, max_digits=4, null=True)),
                ('account_member_verify_status_bank', models.BooleanField(default=False, editable=False)),
                ('account_member_verify_status_bank_filled_date', models.DateTimeField(editable=False, null=True)),
                ('account_member_verify_status_email', models.BooleanField(default=False, editable=False)),
                ('account_member_verify_status_email_filled_date', models.DateTimeField(editable=False, null=True)),
                ('account_member_verify_status_phone_number', models.BooleanField(default=False, editable=False)),
                ('account_member_verify_status_phone_number_filled_date', models.DateTimeField(editable=False, null=True)),
                ('account_member_verify_status_legal_doc_sign', models.BooleanField(default=False, editable=False)),
                ('account_member_verify_status_legal_doc_sign_filled_date', models.DateTimeField(editable=False, null=True)),
                ('account_member_verify_status_subscriber_agreement', models.BooleanField(default=False, editable=False)),
                ('account_member_verify_status_subscriber_agreement_filled_date', models.DateTimeField(auto_now_add=True)),
                ('account_member_verify_status_revision_profile', models.IntegerField(default=0, editable=False)),
                ('account_member_verify_status_revision_profile_last_date', models.DateTimeField(editable=False, null=True)),
                ('account_member_verify_status_revision_profile_check', models.BooleanField(default=False, editable=False)),
                ('account_member_verify_status_created_by', models.CharField(max_length=255, unique=True)),
                ('account_member_verify_status_created_date', models.DateTimeField(auto_now_add=True)),
                ('account_member_verify_status_updated_by', models.CharField(max_length=255)),
                ('account_member_verify_status_updated_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('account_member_verify_status_user_related',),
            },
        ),
        migrations.CreateModel(
            name='AccountPasswordExpired',
            fields=[
                ('account_password_expired_id', models.UUIDField(default=django.contrib.postgres.functions.RandomUUID, editable=False, primary_key=True, serialize=False, unique=True)),
                ('account_password_expired_user_related', models.CharField(max_length=255)),
                ('account_password_expired_last_updated', models.DateTimeField(auto_now_add=True)),
                ('account_password_expired_update_by', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('account_password_expired_id',),
            },
        ),
        migrations.CreateModel(
            name='AccountProfile',
            fields=[
                ('account_profile_id', models.UUIDField(default=django.contrib.postgres.functions.RandomUUID, editable=False, primary_key=True, serialize=False, unique=True)),
                ('account_profile_user_related', models.CharField(editable=False, max_length=255)),
                ('account_profile_phone_number', models.CharField(max_length=15)),
                ('account_profile_identification_number', models.CharField(default=None, max_length=16, null=True, unique=True)),
                ('account_profile_tax_identification_number', models.CharField(default=None, max_length=15, null=True, unique=True)),
                ('account_profile_dob', models.DateField(null=True)),
                ('account_profile_sex', models.CharField(max_length=6, null=True)),
                ('account_profile_address', models.TextField(max_length=500, null=True)),
                ('account_profile_pob', models.CharField(max_length=255, null=True)),
                ('account_profile_address_prov', models.CharField(max_length=255, null=True)),
                ('account_profile_address_district', models.CharField(max_length=255, null=True)),
                ('account_profile_address_sub_district', models.CharField(max_length=255, null=True)),
                ('account_profile_selfie', models.TextField(null=True)),
                ('account_profile_selfie_eidentity', models.TextField(null=True)),
                ('account_profile_eidentity', models.TextField(null=True)),
                ('account_profile_enpwp', models.TextField(null=True)),
                ('account_profile_cif_number', models.IntegerField(null=True, unique=True)),
                ('account_profile_cooperative_number', models.CharField(max_length=255, null=True)),
                ('account_profile_filled_status', models.BooleanField(default=False)),
                ('account_profile_created_by', models.CharField(editable=False, max_length=255)),
                ('account_profile_created_date', models.DateTimeField(auto_now_add=True)),
                ('account_profile_updated_by', models.CharField(max_length=255, null=True)),
                ('account_profile_updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('account_profile_id',),
            },
        ),
        migrations.CreateModel(
            name='AccountReplicationProfile',
            fields=[
                ('account_replication_profile_id', models.UUIDField(default=django.contrib.postgres.functions.RandomUUID, editable=False, primary_key=True, serialize=False, unique=True)),
                ('account_replication_profile_user_related', models.CharField(max_length=255)),
                ('account_replication_profile_phone_number', models.CharField(default=0, max_length=15)),
                ('account_replication_profile_identification_number', models.CharField(default=None, max_length=16, null=True)),
                ('account_replication_profile_tax_identification_number', models.CharField(default=None, max_length=15, null=True)),
                ('account_replication_profile_dob', models.DateField(blank=True, null=True)),
                ('account_replication_profile_sex', models.CharField(max_length=6, null=True)),
                ('account_replication_profile_address', models.TextField(max_length=500, null=True)),
                ('account_replication_profile_pob', models.CharField(editable=False, max_length=255)),
                ('account_replication_profile_address_prov', models.CharField(editable=False, max_length=255)),
                ('account_replication_profile_address_district', models.CharField(editable=False, max_length=255)),
                ('account_replication_profile_address_sub_district', models.CharField(editable=False, max_length=255)),
                ('account_replication_profile_selfie', models.TextField(null=True)),
                ('account_replication_profile_selfie_eidentity', models.TextField(null=True)),
                ('account_replication_profile_eidentity', models.TextField(null=True)),
                ('account_replication_profile_enpwp', models.TextField(null=True)),
                ('account_replication_profile_cif_number', models.IntegerField(editable=False, null=True, unique=True)),
                ('account_replication_profile_cooperative_number', models.IntegerField(editable=False, null=True, unique=True)),
                ('account_replication_profile_filled_status', models.BooleanField(default=False, null=True)),
                ('account_replication_profile_created_by', models.CharField(max_length=255)),
                ('account_replication_profile_created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('account_replication_profile_id',),
            },
        ),
        migrations.CreateModel(
            name='AccountUserPin',
            fields=[
                ('account_user_pin_id', models.UUIDField(default=django.contrib.postgres.functions.RandomUUID, editable=False, primary_key=True, serialize=False, unique=True)),
                ('account_user_pin_related_user', models.CharField(max_length=255)),
                ('account_user_pin_data', models.CharField(editable=False, max_length=255)),
                ('account_user_pin_ip_address', models.CharField(max_length=20)),
                ('account_user_pin_created_by', models.CharField(max_length=255)),
                ('account_user_pin_created_date', models.DateTimeField(auto_now_add=True)),
                ('account_user_pin_updated_by', models.CharField(max_length=255, null=True)),
            ],
            options={
                'ordering': ('account_user_pin_related_user',),
            },
        ),
        migrations.AddIndex(
            model_name='accountuserpin',
            index=models.Index(fields=['account_user_pin_id', 'account_user_pin_related_user'], name='account_acc_account_3f88a3_idx'),
        ),
        migrations.AddIndex(
            model_name='accountreplicationprofile',
            index=models.Index(fields=['account_replication_profile_id', 'account_replication_profile_user_related', 'account_replication_profile_cif_number', 'account_replication_profile_cooperative_number'], name='account_acc_account_30c9cf_idx'),
        ),
        migrations.AddIndex(
            model_name='accountprofile',
            index=models.Index(fields=['account_profile_id', 'account_profile_user_related', 'account_profile_cif_number', 'account_profile_cooperative_number'], name='account_acc_account_b5652b_idx'),
        ),
        migrations.AddIndex(
            model_name='accountpasswordexpired',
            index=models.Index(fields=['account_password_expired_id', 'account_password_expired_user_related'], name='account_acc_account_174ee8_idx'),
        ),
        migrations.AddIndex(
            model_name='accountmemberverifystatus',
            index=models.Index(fields=['account_member_verify_status_id', 'account_member_verify_status_user_related'], name='account_acc_account_fcecc1_idx'),
        ),
        migrations.AddIndex(
            model_name='accountlogresetpassword',
            index=models.Index(fields=['account_log_reset_password_id', 'account_log_reset_password_email'], name='account_acc_account_38f682_idx'),
        ),
        migrations.AddIndex(
            model_name='accountlogchangepassword',
            index=models.Index(fields=['account_log_change_password_id', 'account_log_change_password_username'], name='account_acc_account_1b66b2_idx'),
        ),
        migrations.AddIndex(
            model_name='accountbankusers',
            index=models.Index(fields=['account_bank_user_id', 'account_bank_user_related_to_bank', 'account_bank_user_related_to_user'], name='account_acc_account_9dac77_idx'),
        ),
    ]
