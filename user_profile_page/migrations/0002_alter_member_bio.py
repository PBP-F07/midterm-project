# Generated by Django 4.2.6 on 2023-10-26 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='bio',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
