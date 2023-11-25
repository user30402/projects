import os
from colorama import *

def resm(resmult):
    global mult
    global stat
    if resmult == 0:
        mult = ''
    elif resmult == 1:
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
    stat = round(stat, 3)

def deco():
    print(Style.BRIGHT + Fore.GREEN + '|--------------------|')

while 1 == 1:
    try:
        deco()
        print()
        print('Made by user30402')
        print()
        deco()
        print()
        print('1 - Калькулятор статов; 2 - Кол-во статов на локации.')
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

            if mult == 'K' or mult == 'k' or mult == 'К' or mult == 'к':
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

            resm(resmult)    
            
            stat = round(stat, 2)

            if a == True:

                print(f'У вас будет +{stat}{mult} статы.')
            
            elif a == False:

                print('Ошибка! Укажите верный промежуток во времени! ')

        elif choice == '2':
            
            print('1 - FS; 2 - BT; 3 - MS/JF; 4 - PP.')
            print()
            choice = input('Введите пункт: ')
            print()
            if choice == '1':
                print('1 - Rock; 2 - Crystal; 3 - Blue God Star; 4 - Green God Star; 5 - Red God Star; 6 - Meteorite; 7 - SO; 8 - HR; 9 - FM; 10 - BH; 11 - CL; 12 - DC; 13 - NI; 14 - TC; 15 - SH.')
                print()
                choice = input('Введите пункт: ')
                print()
                mult = int(input('Введите Ваш множитель на Fist Strenght: '))
                print()

                if choice == '1':
                    mult *= 10
                elif choice == '2':
                    mult *= 100
                elif choice == '3':
                    mult *= 2000
                elif choice == '4':
                    mult *= 40000
                elif choice == '5':
                    mult *= 800000
                elif choice == '6':
                    mult *= 6000000
                elif choice == '7':
                    mult *= 300000000
                elif choice == '8':
                    mult *= 21000000000
                elif choice == '9':
                    mult *= 2308000000000
                elif choice == '10':
                    mult *= 347500000000000
                elif choice == '11':
                    mult *= 52000000000000000
                elif choice == '12':
                    mult *= 7800000000000000000
                elif choice == '13':
                    mult *= 1170000000000000000000
                elif choice == '14':
                    mult *= 175500000000000000000000
                elif choice == '15':
                    mult *= 21050000000000000000000000

                stat = mult
                resmult = 0

                while stat > 1000:
                    stat /= 1000
                    resmult += 1

                resm(resmult)

                print(f'Вы будете получать {stat}{mult} за тик.')

            elif choice == '2':
                print('1 - Ice Bath; 2 - Fire Bath; 3 - Iceberg; 4 - Tornado; 5 - Volcano; 6 - Hellfire; 7 - Green Acid; 8 - Red Acid; 9 - ToH; 10 - TC; 11 - EJ; 12 - GG; 13 - DA; 14 - Sailboat; 15 - TS.')
                print()
                choice = input('Введите пункт: ')
                print()
                mult = int(input('Введите Ваш множитель на Body Toughness: '))
                print()
                if choice == '1':
                    mult *= 5
                elif choice == '2':
                    mult *= 10
                elif choice == '3':
                    mult *= 20
                elif choice == '4':
                    mult *= 50
                elif choice == '5':
                    mult *= 100
                elif choice == '6':
                    mult *= 2000
                elif choice == '7':
                    mult *= 40000
                elif choice == '8':
                    mult *= 800000
                elif choice == '9':
                    mult *= 6000000
                elif choice == '10':
                    mult *= 180000000
                elif choice == '11':
                    mult *= 5500000000
                elif choice == '12':
                    mult *= 162500000000
                elif choice == '13':
                    mult *= 5000000000000
                elif choice == '14':
                    mult *= 150000000000000
                elif choice == '15':
                    mult *= 4500000000000000

                stat = mult
                resmult = 0

                while stat > 1000:
                    stat /= 1000
                    resmult += 1

                resm(resmult)
                
                print(f'Вы будете получать {stat}{mult} за тик.')

            elif choice == '3':
                print('1 - 100 Lb; 2 - 1 Ton; 3 - 10 Ton; 4 - 100 Ton; 5 - 1K Ton; 6 - 10K Ton; 7 - 100K Ton; 8 - 1M Ton; 9 - 10M Ton; 10 - 1B Ton.')
                print()
                choice = input('Введите пункт: ')
                print()
                mult = int(input('Введите Ваш множитель на MS/JF: '))
                print()
                if choice == '1':
                    mult *= 2
                elif choice == '2':
                    mult *= 5
                elif choice == '3':
                    mult *= 10
                elif choice == '4':
                    mult *= 20
                elif choice == '5':
                    mult *= 150
                elif choice == '6':
                    mult *= 750
                elif choice == '7':
                    mult *= 3500
                elif choice == '8':
                    mult *= 18000
                elif choice == '9':
                    mult *= 90000
                elif choice == '10':
                    mult *= 400000

                stat = mult
                resmult = 0

                while stat > 1000:
                    stat /= 1000
                    resmult += 1

                resm(resmult)
                
                print(f'Вы будете получать {stat}{mult} за тик.')

            elif choice == '4':
                print('1 - 1M PP Zone; 2 - 1B PP Zone; 3 - 1T PP Zone; 4 - 1Qa PP Zone; 5 - GS; 6 - EC; 7 - FG; 8 - PI; 9 - NH; 10 - FF; 11 - Megalodon; 12 - GG; 13 - GS; 14 - TV.')
                print()
                choice = input('Введите пункт: ')
                print()
                mult = int(input('Введите Ваш множитель на Psychic Power: '))
                print()
                if choice == '1':
                    mult *= 100
                elif choice == '2':
                    mult *= 10000
                elif choice == '3':
                    mult *= 1000000
                elif choice == '4':
                    mult *= 100000000
                elif choice == '5':
                    mult *= 2500000000
                elif choice == '6':
                    mult *= 250000000000
                elif choice == '7':
                    mult *= 25000000000000
                elif choice == '8':
                    mult *= 2500000000000000
                elif choice == '9':
                    mult *= 250000000000000000
                elif choice == '10':
                    mult *= 25000000000000000000
                elif choice == '11':
                    mult *= 2500000000000000000000
                elif choice == '12':
                    mult *= 250000000000000000000000
                elif choice == '13':
                    mult *= 25000000000000000000000000
                elif choice == '14':
                    mult *= 2500000000000000000000000000

                stat = mult
                resmult = 0

                while stat > 1000:
                    stat /= 1000
                    resmult += 1

                resm(resmult)
                
                print(f'Вы будете получать {stat}{mult} за тик.')

        print()
        deco()
        print()
        print('Discord - user30402.638')
        print()
        deco()
        print()
        input('Нажмите Enter для очистки консоли...')
        os.system('cls')
    except:
        print()
        deco()
        print()
        print(Style.BRIGHT + Fore.RED + 'Неизвестная ошибка!')
        print()
        deco()
        print()
        input('Нажмите Enter для очистки консоли...')
        os.system('cls')
