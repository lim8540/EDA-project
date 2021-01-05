# Generated by Django 3.1.4 on 2021-01-03 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('total_game', models.IntegerField()),
                ('home_game', models.IntegerField()),
                ('away_game', models.IntegerField()),
                ('home_win', models.IntegerField()),
                ('away_win', models.IntegerField()),
                ('total_winning_rate', models.FloatField()),
                ('home_winning_rate', models.FloatField()),
                ('away_winning_rate', models.FloatField()),
            ],
        ),
    ]
