# Generated by Django 4.2.6 on 2023-10-28 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_details', '0005_remove_reply_discus_reply_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion',
            name='date_added',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='reply',
            name='date_add',
            field=models.CharField(default='', max_length=255),
        ),
    ]
