# Generated by Django 4.2.6 on 2023-10-26 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingPage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='amount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]