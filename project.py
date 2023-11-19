import os

def deco():
    print('|--------------------|')

while 1 == 1:

    deco()
    print()
    print('Made by user30402')
    print()
    deco()
    print()
    mult = input('Укажите величину статы (K, M, B, T, Qa, Qi): ')
    print()
    getstat = float(input('Укажите кол-во статы за тик: '))
    print()
    delay = float(input('Укажите промежуток между получением статы в секундах (1.5 или 1): '))
    print()
    timemult = input('Укажите множитель времени для фарма (М, Ч, Д): ')
    print()
    time = float(input('Укажите время для афк: '))
    print()
    deco()
    print()

    if timemult == 'М' or timemult == 'м' or timemult == 'M' or timemult == 'm':
        time *= 60
    elif timemult == 'Ч' or timemult == 'ч' or timemult == 'H' or timemult == 'h':
        time *= 3600
    elif timemult == 'Д' or timemult == 'д' or timemult == 'D' or timemult == 'd':
        time *= 86400

    if delay == 1.5:
        time *= 0.80

    if mult == 'K' or mult == 'k' or mult == 'к' or mult == 'К':
        getstat *= 1000
        res = 1000
        resmult = 1
    elif mult == 'M' or mult == 'm' or mult == 'М' or mult == 'м':
        getstat *= 1000000
        res = 1000000
        resmult = 2
    elif mult == 'B' or mult == 'b' or mult == 'В' or mult == 'в':
        getstat *= 1000000000
        res = 1000000000
        resmult = 3
    elif mult == 'T' or mult == 't' or mult == 'Т' or mult == 'т':
        getstat *= 1000000000000
        res = 1000000000000
        resmult = 4
    elif mult == 'Qa' or mult == 'qA' or mult == 'QA' or mult == 'qa':
        getstat *= 1000000000000000
        res = 1000000000000000
        resmult = 5
    elif mult == 'Qi' or mult == 'qI' or mult == 'QI' or mult == 'qi':
        getstat *= 1000000000000000000
        res = 1000000000000000000
        resmult = 6

    stat = getstat
    stat *= time
    stat /= res

    while stat > 1000:
        stat /= 1000
        resmult += 1

    if resmult == 1:
        mult = 'K'
    elif resmult == 2:
        mult = 'M'
    elif resmult == 3:
        mult = 'B'
    elif resmult == 4:
        mult = 'T'
    elif resmult == 5:
        mult = 'Qa'
    elif resmult == 6:
        mult = 'Qi'
    
    stat = round(stat, 2)

    print(f'У вас будет +{stat}{mult} статы.')
    print()
    deco()
    print()
    print('Discord - user30402.638')
    print()
    deco()
    print()
    input('Нажмите Enter для очистки консоли...')
    os.system('cls')
