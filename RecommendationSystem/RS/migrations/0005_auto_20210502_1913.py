# Generated by Django 3.1.7 on 2021-05-02 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RS', '0004_auto_20210502_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='Email',
            field=models.CharField(max_length=90, null=True),
        ),
    ]
