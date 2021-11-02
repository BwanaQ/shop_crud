# Generated by Django 3.2.8 on 2021-10-27 07:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('units', '0003_unit_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='units', to=settings.AUTH_USER_MODEL),
        ),
    ]
