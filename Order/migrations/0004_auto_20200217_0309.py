# Generated by Django 2.2.6 on 2020-02-17 03:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0003_auto_20200215_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
