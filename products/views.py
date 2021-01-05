from django.shortcuts import render, HttpResponse
from .models import Nation, Data
import csv
import pandas as pd

# Create your views here.


def csvToModel(request):
    path = '/Users/sumin/project/programmers/pandas_django/src/csv/match_by_nation.csv'
    file = open(path)
    reader = csv.reader(file)
    next(reader)
    #print('-----', reader)
    list = []
    for row in reader:
        list.append(Nation(
            name = row[0],
            total_game = row[1],
            home_game = row[2],
            away_game = row[3],
            home_win = row[4],
            away_win = row[5],
            total_winning_rate = row[6],
            home_winning_rate = row[7],
            away_winning_rate = row[8],
            gap = float(row[7]) - float(row[8])
        ))
    Nation.objects.bulk_create(list)
    return HttpResponse('create model...')

def csvToModel2(request):
    path = '/Users/sumin/project/programmers/pandas_django/src/csv/results.csv'
    file = open(path)
    reader = csv.reader(file)
    next(reader)
    home_win = 0
    away_win = 0
    draw = 0
    for row in reader:
        if(row[8] == 'FALSE'):
            if row[3] > row[4]:
                home_win += 1
            elif row[3] < row[4]:
                away_win += 1
            else:
                draw += 1
    list = []
    list.append(Data(
        name = 'base_data',
        Home_win = home_win,
        Away_win = away_win,
        Draw = draw
    ))
    Data.objects.bulk_create(list)

    return HttpResponse('Create model...')

def main(request):
    nation_db = Nation.objects.order_by('-total_game')[:15]
    basic_data = Data.objects.all()
    min_db = Nation.objects.order_by('gap')[:15]
    print(min_db)
    return render(request, 'main.html', {'database':nation_db, 'basic_data' : basic_data, 'gap_data' : min_db}) 

