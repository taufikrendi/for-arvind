# Generated by Django 3.1.5 on 2021-06-25 21:55

import utils.generator
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogNodeflux',
            fields=[
                ('log_nodeflux_id', models.CharField(default=account.generator.generator_uuid, editable=False, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('log_nodeflux_job_id', models.CharField(max_length=255)),
                ('log_nodeflux_status', models.CharField(max_length=255)),
                ('log_nodeflux_analytic_type', models.CharField(max_length=255)),
                ('log_nodeflux_message', models.CharField(max_length=255)),
                ('log_nodeflux_ok', models.CharField(max_length=255)),
                ('log_nodeflux_produce', models.BooleanField(editable=False)),
                ('log_nodeflux_consume_status_job_id', models.CharField(max_length=255)),
                ('log_nodeflux_consume_status_status', models.CharField(max_length=255)),
                ('log_nodeflux_consume_status_analytic_type', models.CharField(max_length=255)),
                ('log_nodeflux_consume_status_message', models.CharField(max_length=255)),
                ('log_nodeflux_consume_status_ok', models.CharField(max_length=255)),
                ('log_nodeflux_consume_status_similarity', models.DecimalField(decimal_places=2, editable=False, max_digits=4, null=True)),
                ('log_nodeflux_consume_status', models.BooleanField(editable=False)),
                ('log_nodeflux_date', models.DateTimeField(default=datetime.datetime.now, editable=False)),
            ],
            options={
                'ordering': ('-log_nodeflux_date',),
            },
        ),
    ]
