# Generated by Django 2.0.7 on 2018-08-26 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0014_auto_20180823_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='头像'),
        ),
    ]
