# Generated by Django 3.0.7 on 2021-05-27 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cofee',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
