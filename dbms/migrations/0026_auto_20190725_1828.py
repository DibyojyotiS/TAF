# Generated by Django 2.2.2 on 2019-07-25 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbms', '0025_auto_20190709_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='password',
            field=models.CharField(max_length=194),
        ),
    ]
