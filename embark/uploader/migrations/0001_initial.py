# Generated by Django 4.1.3 on 2022-11-04 10:39

import datetime
from django.db import migrations, models
import django.utils.datetime_safe
import uploader.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(blank=True, help_text='Device name', max_length=127, verbose_name='Device name')),
                ('device_date', models.DateTimeField(blank=True, default=django.utils.datetime_safe.datetime.now)),
                ('visible', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['device_name'],
            },
        ),
        migrations.CreateModel(
            name='FirmwareAnalysis',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('pid', models.BigIntegerField(blank=True, help_text='process id of subproc', null=True, verbose_name='PID')),
                ('firmware_name', models.CharField(default='File unknown', max_length=127)),
                ('version', uploader.models.CharFieldExpertMode(blank=True, help_text='Firmware version', max_length=127, verbose_name='Firmware version')),
                ('notes', uploader.models.CharFieldExpertMode(blank=True, help_text='Testing notes', max_length=127, verbose_name='Testing notes')),
                ('firmware_Architecture', uploader.models.CharFieldExpertMode(blank=True, choices=[(None, 'Select architecture'), ('MIPS', 'MIPS'), ('ARM', 'ARM'), ('x86', 'x86'), ('x64', 'x64'), ('PPC', 'PPC')], help_text='Architecture of the linux firmware [MIPS, ARM, x86, x64, PPC] -a will be added', max_length=127, verbose_name='Select architecture of the linux firmware')),
                ('user_emulation_test', uploader.models.BooleanFieldExpertMode(blank=True, default=False, help_text='Enables automated qemu emulation tests')),
                ('system_emulation_test', uploader.models.BooleanFieldExpertMode(blank=True, default=False, help_text='Enables automated qemu system emulation tests')),
                ('deep_extraction', uploader.models.BooleanFieldExpertMode(blank=True, default=False, help_text='Enable deep extraction - try to extract every file two times with binwalk')),
                ('cwe_checker', uploader.models.BooleanFieldExpertMode(blank=True, default=False, help_text='Enables cwe-checker')),
                ('online_checks', uploader.models.BooleanFieldExpertMode(blank=True, default=False, help_text='Activate online checks (e.g. upload and test with VirusTotal)')),
                ('path_to_logs', models.FilePathField(blank=True, default='/')),
                ('start_date', models.DateTimeField(blank=True, default=django.utils.datetime_safe.datetime.now)),
                ('end_date', models.DateTimeField(blank=True, default=datetime.datetime(1, 1, 1, 0, 0))),
                ('scan_time', models.DurationField(blank=True, default=datetime.timedelta(0))),
                ('duration', models.CharField(blank=True, max_length=100, null=True)),
                ('finished', models.BooleanField(default=False)),
                ('failed', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='FirmwareFile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('is_archive', models.BooleanField(blank=True, default=False)),
                ('upload_date', models.DateTimeField(blank=True, default=django.utils.datetime_safe.datetime.now)),
                ('file', models.FileField(upload_to=uploader.models.FirmwareFile.get_storage_path)),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_name', models.CharField(blank=True, help_text='label name', max_length=127, unique=True, verbose_name='label name')),
                ('label_date', models.DateTimeField(blank=True, default=django.utils.datetime_safe.datetime.now)),
            ],
            options={
                'ordering': ['label_name'],
            },
        ),
        migrations.CreateModel(
            name='ResourceTimestamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.datetime_safe.datetime.now)),
                ('cpu_percentage', models.FloatField(default=0.0)),
                ('memory_percentage', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(blank=True, help_text='Vendor name', max_length=127, unique=True, verbose_name='vendor name')),
            ],
            options={
                'ordering': ['vendor_name'],
            },
        ),
    ]
