# Generated by Django 3.1.7 on 2021-05-11 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RS', '0007_remove_patient_fullname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.TextField(null=True)),
            ],
        ),
    ]
