# Generated by Django 2.2.6 on 2020-02-19 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_auto_20200217_1139'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courserecord',
            options={'ordering': ['id'], 'verbose_name': '上课记录', 'verbose_name_plural': '上课记录'},
        ),
        migrations.AlterModelOptions(
            name='studyrecord',
            options={'ordering': ['id'], 'verbose_name': '学习记录', 'verbose_name_plural': '学习记录'},
        ),
        migrations.AddField(
            model_name='userprofile',
            name='stu_account',
            field=models.ForeignKey(blank=True, help_text='只有学员报名后才可为其创建账户', null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Customer', verbose_name='关联学员账号'),
        ),
    ]
