from datetime import datetime
from django.db import models

from utils.generator import generator_uuid
from utils.validators import numeric


# Create your models here.
class Banks(models.Model):
    bank_id = models.CharField(
        primary_key=True, default=generator_uuid, max_length=255, editable=False, unique=True)
    bank_name = models.CharField(max_length=30, null=False)
    bank_code = models.CharField(max_length=3, null=False, unique=True, validators=[numeric])
    bank_created_by = models.CharField(max_length=255, null=False)
    bank_created_date = models.DateTimeField(
        editable=False, null=False, default=datetime.now)
    bank_updated_by = models.CharField(max_length=255, null=False)
    bank_updated_at = models.DateTimeField(auto_now_add=False, null=True)

    def __str__(self):
        return self.bank_name

    def __unicode__(self):
        return '%s' % self.bank_name

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.bank_id), escape(self.bank_name),
            escape(self.bank_code), escape(self.bank_created_date),
            escape(self.bank_created_by), escape(self.bank_updated_at),
            escape(self.bank_updated_by)
        )

    class Meta:
        ordering = ('bank_code',)


class Province(models.Model):
    province_id = models.CharField(
        primary_key=True, default=generator_uuid, max_length=255, editable=False, unique=True)
    province_name = models.CharField(max_length=30, null=False)
    province_code = models.CharField(max_length=3, null=False, unique=True, validators=[numeric])
    province_created_by = models.CharField(max_length=255, null=False)
    province_created_date = models.DateTimeField(
        editable=False, null=False, default=datetime.now)
    province_updated_by = models.CharField(max_length=255, null=False)
    province_updated_at = models.DateTimeField(auto_now_add=False, null=True)

    def __str__(self):
        return self.province_name

    def __unicode__(self):
        return '%s' % self.province_name

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.province_id), escape(self.province_name),
            escape(self.province_code), escape(self.province_created_date),
            escape(self.province_created_by), escape(self.province_updated_at),
            escape(self.province_updated_by)
        )

    class Meta:
        ordering = ('province_name',)


class District(models.Model):
    district_id = models.CharField(
        primary_key=True, default=generator_uuid, max_length=255, editable=False, unique=True)
    district_name = models.CharField(max_length=30, null=False)
    district_code = models.CharField(max_length=4, null=False, validators=[numeric])
    district_relation = models.ForeignKey(Province, on_delete=models.CASCADE)
    district_created_by = models.CharField(max_length=255, null=False)
    district_created_date = models.DateTimeField(
        editable=False, null=False, default=datetime.now)
    district_updated_by = models.CharField(max_length=255, null=False)
    district_updated_at = models.DateTimeField(auto_now_add=False, null=True)

    def __str__(self):
        return self.district_name

    def __unicode__(self):
        return '%s' % self.district_name

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.district_id), escape(self.district_name),
            escape(self.district_code), escape(self.district_relation),
            escape(self.district_created_date), escape(self.district_created_by),
            escape(self.district_updated_at), escape(self.district_updated_by)
        )

    class Meta:
        ordering = ('district_name',)


class SubDistrict(models.Model):
    sub_district_id = models.CharField(
        primary_key=True, default=generator_uuid, max_length=255, editable=False, unique=True)
    sub_district_name = models.CharField(max_length=30, null=False)
    sub_district_relation = models.ForeignKey(District, on_delete=models.CASCADE)
    sub_district_code = models.CharField(max_length=7, null=False, validators=[numeric])
    sub_district_created_by = models.CharField(max_length=255, null=False)
    sub_district_created_date = models.DateTimeField(
        editable=False, null=False, default=datetime.now)
    sub_district_updated_by = models.CharField(max_length=255, null=False)
    sub_district_updated_at = models.DateTimeField(auto_now_add=False, null=True)

    def __str__(self):
        return self.sub_district_name

    def __unicode__(self):
        return '%s' % self.sub_district_name

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.sub_district_id), escape(self.sub_district_name),
            escape(self.sub_district_relation), escape(self.sub_district_code),
            escape(self.sub_district_created_by), escape(self.sub_district_created_date),
            escape(self.sub_district_updated_at), escape(self.sub_district_updated_by)
        )

    class Meta:
        ordering = ('sub_district_name',)


class LogNodeflux(models.Model):
    log_nodeflux_id = models.CharField(
        primary_key=True, default=generator_uuid, max_length=255, editable=False, unique=True)
    log_nodeflux_job_id = models.CharField(max_length=255)
    log_nodeflux_status = models.CharField(max_length=255)
    log_nodeflux_analytic_type = models.CharField(max_length=255)
    log_nodeflux_message = models.CharField(max_length=255)
    log_nodeflux_ok = models.CharField(max_length=255)
    log_nodeflux_produce = models.BooleanField(editable=False, null=False)
    log_nodeflux_consume_status_job_id = models.CharField(max_length=255)
    log_nodeflux_consume_status_status = models.CharField(max_length=255)
    log_nodeflux_consume_status_analytic_type = models.CharField(max_length=255)
    log_nodeflux_consume_status_message = models.CharField(max_length=255)
    log_nodeflux_consume_status_ok = models.CharField(max_length=255)
    log_nodeflux_consume_status_similarity = models.DecimalField(max_digits=4, decimal_places=2, null=True, editable=False)
    log_nodeflux_consume_status = models.BooleanField(editable=False, null=False)
    log_nodeflux_date = models.DateTimeField(
        editable=False, null=False, default=datetime.now)

    def __str__(self):
        return self.log_nodeflux_id

    def __unicode__(self):
        return '%s' % self.log_nodeflux_id

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.log_nodeflux_id), escape(self.log_nodeflux_job_id),
            escape(self.log_nodeflux_status), escape(self.log_nodeflux_analytic_type),
            escape(self.log_nodeflux_message), escape(self.log_nodeflux_ok),
            escape(self.log_nodeflux_produce), escape(self.log_nodeflux_consume_status_job_id),
            escape(self.log_nodeflux_consume_status_status), escape(self.log_nodeflux_consume_status_analytic_type),
            escape(self.log_nodeflux_consume_status_message), escape(self.log_nodeflux_consume_status_ok),
            escape(self.log_nodeflux_consume_status), escape(self.log_nodeflux_date),
            escape(self.log_nodeflux_consume_status_similarity)
        )

    class Meta:
        ordering = ('-log_nodeflux_date',)