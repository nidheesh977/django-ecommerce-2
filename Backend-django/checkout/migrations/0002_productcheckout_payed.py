# Generated by Django 3.1 on 2021-08-31 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcheckout',
            name='payed',
            field=models.BooleanField(default=False),
        ),
    ]