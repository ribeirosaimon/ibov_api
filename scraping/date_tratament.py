from datetime import datetime


def date_treatment():
    weekday = datetime.today().weekday()
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    if month == 1:
        month = 'Jan'
    if month == 2:
        month = 'Fev'
    if month == 3:
        month = 'Mar'
    if month == 4:
        month = 'Abr'
    if month == 5:
        month = 'Mai'
    if month == 6:
        month = 'Jun'
    if month == 7:
        month = 'Jul'
    if month == 8:
        month = 'Ago'
    if month == 9:
        month = 'Set'
    if month == 10:
        month = 'Out'
    if month == 11:
        month = 'Nov'
    if month == 12:
        month = 'Dez'

    if weekday == 5:
        day = day - 1
    if weekday == 6:
        day = day - 2
    #if weekday ==0:
    #    day = day -3

    if len(str(day)) == 1:
        day = f'0{day}'

    return f'{month} {day}, {year}'

date = 'Jul 10, 2020'

def dataIso():
    weekday = datetime.today().weekday()
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day

    if weekday == 5:
        day = day - 1
    if weekday == 6:
        day = day - 2


    return f'{year}:{month}:{day}'
