# Generated by Django 2.1.1 on 2018-10-02 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_estimator', '0002_auto_20181002_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='skill',
            field=models.TextField(),
        ),
    ]
