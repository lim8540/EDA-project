# Generated by Django 3.1.4 on 2021-01-05 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210103_0748'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('Home_win', models.IntegerField()),
                ('Away_win', models.IntegerField()),
                ('Draw', models.IntegerField()),
            ],
        ),
    ]
