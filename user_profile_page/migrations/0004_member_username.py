# Generated by Django 4.2.5 on 2023-12-11 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile_page', '0003_alter_member_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]