# Generated by Django 3.1.7 on 2021-05-02 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RS', '0003_auto_20210502_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='username',
        ),
        migrations.AlterField(
            model_name='patient',
            name='Email',
            field=models.TextField(max_length=90, null=True),
        ),
    ]
