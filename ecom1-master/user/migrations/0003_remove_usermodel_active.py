# Generated by Django 2.2.4 on 2019-10-02 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_usermodel_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='active',
        ),
    ]
