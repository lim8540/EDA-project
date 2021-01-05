from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 220)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.name)

class Nation(models.Model):
    name = models.CharField(max_length = 20)
    total_game = models.IntegerField()
    home_game = models.IntegerField()
    away_game = models.IntegerField()
    home_win = models.IntegerField()
    away_win = models.IntegerField()
    total_winning_rate = models.FloatField()
    home_winning_rate = models.FloatField()
    away_winning_rate = models.FloatField()
    gap = models.FloatField(default = 0.)

    def __str__(self):
        return str(self.name)

class Data(models.Model):
    name = models.CharField(max_length = 20)
    Home_win = models.IntegerField()
    Away_win = models.IntegerField()
    Draw = models.IntegerField()

    def __str__(self):
        return str(self.name)