# Generated by Django 2.0.7 on 2018-08-15 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0008_auto_20180812_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='ctime',
            field=models.DateTimeField(auto_now=True, verbose_name='创建时间'),
        ),
    ]
