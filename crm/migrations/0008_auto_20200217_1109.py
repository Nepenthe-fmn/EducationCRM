# Generated by Django 2.2.6 on 2020-02-17 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_userprofile_roles'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='常用邮箱'),
        ),
        migrations.AddField(
            model_name='customer',
            name='id_num',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
