# Generated by Django 4.2.6 on 2023-10-28 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist_page', '0002_wishlistitem_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlistitem',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]