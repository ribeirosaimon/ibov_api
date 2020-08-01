import datetime


def date_treatment(tempo=0):
    weekday = datetime.datetime.today().weekday()
    hoje = datetime.datetime.now() - datetime.timedelta(tempo)
    ontem = datetime.timedelta(1)
    anteontem = datetime.timedelta(2)
    hora_do_dia = int(datetime.datetime.now().strftime('%H'))

    if weekday == 5:
        dia_para_tratamento = hoje - ontem
    elif weekday == 6:
        dia_para_tratamento = hoje - anteontem
    elif weekday == 0:
        if hora_do_dia < 10:
            dia_para_tratamento = hoje - ontem - anteontem
    else:
        if hora_do_dia < 10:
            dia_para_tratamento = hoje - ontem

    month = int(str(dia_para_tratamento)[5:7])
    day = int(str(dia_para_tratamento)[8:10])
    year = int(str(dia_para_tratamento)[0:4])

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

    return f'{month} {day}, {year}'


def dataIso():
    weekday = datetime.datetime.today().weekday()
    hoje = datetime.datetime.now() - datetime.timedelta()
    ontem = datetime.timedelta(1)
    anteontem = datetime.timedelta(2)
    hora_do_dia = int(datetime.datetime.now().strftime('%H'))

    if weekday == 5:
        dia_para_tratamento = hoje - ontem
    elif weekday == 6:
        dia_para_tratamento = hoje - anteontem
    elif weekday == 0:
        if hora_do_dia < 10:
            dia_para_tratamento = hoje - ontem - anteontem
    else:
        if hora_do_dia < 10:
            dia_para_tratamento = hoje - ontem

    month = int(str(dia_para_tratamento)[5:7])
    day = int(str(dia_para_tratamento)[8:10])
    year = int(str(dia_para_tratamento)[0:4])

    return f'{year}:{month}:{day}'


def date_tweet_sentiment_mes_anterior():
    weekday = datetime.today().weekday()
    now = datetime.now()
    year = now.year
    month = now.month - 1
    day = now.day
    hour = now.strftime('%H')

    return f'{year}-{month}-{day}'
