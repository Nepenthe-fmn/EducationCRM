# Generated by Django 2.2.6 on 2020-02-15 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_auto_20200215_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='roles',
            field=models.ManyToManyField(blank=True, null=True, to='crm.Role'),
        ),
    ]
