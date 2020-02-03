# Generated by Django 3.0.2 on 2020-01-31 12:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='assigned_to',
            field=models.ManyToManyField(related_name='lead_assigned_salespersonusers', to=settings.AUTH_USER_MODEL),
        ),
    ]