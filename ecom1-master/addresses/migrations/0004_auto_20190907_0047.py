# Generated by Django 2.2.4 on 2019-09-06 19:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0003_auto_20190905_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressmodel',
            name='billing_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.BillingProfile'),
            preserve_default=False,
        ),
    ]
