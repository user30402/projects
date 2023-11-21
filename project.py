import os
from datetime import datetime

curdate = datetime.now()

def deco():
    print('|--------------------|')

while 1 == 1:

    deco()
    print()
    print('Made by user30402')
    print()
    deco()
    print()
    print('1 - Калькулятор статов.')
    print()
    choice = input('Введите пункт: ')
    print()
    if choice == '1':
        mult = input('Укажите величину статы (K, M, B, T, Qa, Qi, Sx, Sp, Oc, No, De, Ud, Dd, Td): ')
        print()
        getstat = float(input('Укажите кол-во статы за тик: '))
        print()
        delay = float(input('Укажите промежуток между получением статы в секундах (0.5, 1 или 1.5): '))
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
            time *= (60 * 60)
        elif timemult == 'Д' or timemult == 'д' or timemult == 'D' or timemult == 'd':
            time *= (60 * 60 * 24)

        if delay == 1.5:
            time *= 0.80
            a = True
        elif delay == 0.5:
            time *= 2
            a = True
        elif delay == 1:
            time *= 1
            a = True
        else:
            a = False

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
        elif mult == 'Sx' or mult == 'sX' or mult == 'SX' or mult == 'sx':
            getstat *= 1000000000000000000000
            res = 1000000000000000000000
            resmult = 7
        elif mult == 'Sp' or mult == 'sP' or mult == 'SP' or mult == 'sp':
            getstat *= 1000000000000000000000000
            res = 1000000000000000000000000
            resmult = 8
        elif mult == 'Oc' or mult == 'oC' or mult == 'OC' or mult == 'oc':
            getstat *= 1000000000000000000000000000
            res = 1000000000000000000000000000
            resmult = 9
        elif mult == 'No' or mult == 'nO' or mult == 'NO' or mult == 'no':
            getstat *= 1000000000000000000000000000000
            res = 1000000000000000000000000000000
            resmult = 10
        elif mult == 'De' or mult == 'dE' or mult == 'DE' or mult == 'de':
            getstat *= 1000000000000000000000000000000000
            res = 1000000000000000000000000000000000
            resmult = 11
        elif mult == 'Ud' or mult == 'uD' or mult == 'UD' or mult == 'ud':
            getstat *= 1000000000000000000000000000000000000
            res = 1000000000000000000000000000000000000
            resmult = 12
        elif mult == 'Dd' or mult == 'dD' or mult == 'DD' or mult == 'dd':
            getstat *= 1000000000000000000000000000000000000000
            res = 1000000000000000000000000000000000000000
            resmult = 13
        elif mult == 'Td' or mult == 'tD' or mult == 'TD' or mult == 'td':
            getstat *= 1000000000000000000000000000000000000000000
            res = 1000000000000000000000000000000000000000000
            resmult = 14

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
        elif resmult == 7:
            mult = 'Sx'
        elif resmult == 8:
            mult = 'Sp'
        elif resmult == 9:
            mult = 'Oc'
        elif resmult == 10:
            mult = 'No'
        elif resmult == 11:
            mult = 'De'
        elif resmult == 12:
            mult = 'Ud'
        elif resmult == 13:
            mult = 'Dd'
        elif resmult == 14:
            mult = 'Td'
        else:
            mult = 'n/a'
        
        stat = round(stat, 2)

        if a == True:

            print(f'У вас будет +{stat}{mult} статы.')
            print()
            print(f'Запрос был оформлен в {curdate.hour}:{curdate.minute}.')
        
        elif a == False:

            print('Ошибка! Укажите верный промежуток во времени! ')

    print()
    deco()
    print()
    print('Discord - user30402.638')
    print()
    deco()
    print()
    input('Нажмите Enter для очистки консоли...')
    os.system('cls')
