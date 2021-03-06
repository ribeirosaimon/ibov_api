import datetime


def date_treatment(tempo=0):
    #Pegando os dias da semana, caso o for antes da abertura do mercado (10 horas)
    #ou fim de semana, vai se pegar o ultimo dia util
    weekday = datetime.datetime.today().weekday()
    hoje = datetime.datetime.now() - datetime.timedelta(tempo)
    ontem = datetime.timedelta(1)
    anteontem = datetime.timedelta(2)
    hora_do_dia = int(datetime.datetime.now().strftime('%H'))

    if weekday == 5:
        hoje = hoje - ontem
    elif weekday == 6:
        hoje = hoje - anteontem
    elif weekday == 0:
        if hora_do_dia < 10:
            hoje = hoje - ontem - anteontem
    else:
        if hora_do_dia < 10:
            hoje = hoje - ontem

    #deve se pegar os dias para transformar no formato do scraping
    month = int(str(hoje)[5:7])
    day = int(str(hoje)[8:10])
    year = int(str(hoje)[0:4])

    #o dia deve haver 2 digitos
    if len(str(day)) != 2:
        day = f'0{day}'

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
        month = 'Aug'
    if month == 9:
        month = 'Sep'
    if month == 10:
        month = 'Oct'
    if month == 11:
        month = 'Nov'
    if month == 12:
        month = 'Dec'

    return f'{month} {day}, {year}'


def dataIso(data_string):

    month = data_string[0:3]
    day = data_string[4:6]
    year = data_string[8:12]

    if month == 'Jan':
        month = 1
    if month == 'Fev':
        month = 2
    if month == 'Mar':
        month = 3
    if month == 'Abr':
        month = 4
    if month == 'Mai':
        month = 5
    if month == 'Jun':
        month = 6
    if month == 'Jul':
        month = 7
    if month == 'Aug':
        month = 8
    if month == 'Sep':
        month = 9
    if month == 'Oct':
        month = 10
    if month == 'Nov':
        month = 11
    if month == 'Dec':
        month = 12

    return f'{year}:{month}:{day}'



def date_timestamp_for_date_utc():
    data_atual = str(datetime.date.today())
    data_atual = data_atual.split('-')
    ano = int(data_atual[0])
    ano_passado = ano - 1
    mes = int(data_atual[1])
    dia = int(data_atual[2])
    dt_ano_atual = datetime.datetime(ano, mes, dia)
    dt_ano_passado = datetime.datetime(ano_passado, mes, dia)
    timestamp_ano_atual = (dt_ano_atual - datetime.datetime(1970, 1, 1)).total_seconds()
    timestamp_ano_passado = (dt_ano_passado - datetime.datetime(1970,1,1)).total_seconds()
    ts_atual = int(timestamp_ano_atual)
    ts_passado = int(timestamp_ano_passado)
    #datetime.datetime.utcfromtimestamp(ts_atual).strftime('%Y-%m-%d %H:%M:%S')
    return ts_atual, ts_passado

def data_atual():
    return str(datetime.date.today())
