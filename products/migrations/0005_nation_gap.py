# Generated by Django 3.1.4 on 2021-01-05 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='nation',
            name='gap',
            field=models.FloatField(default=0.0),
        ),
    ]