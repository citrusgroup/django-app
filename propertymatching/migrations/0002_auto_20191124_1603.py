# Generated by Django 2.2.7 on 2019-11-24 16:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('propertymatching', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listingitem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listingitem',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
