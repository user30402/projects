import math, os, webbrowser as wb
from colorama import *

def s():
    print(Style.BRIGHT + Fore.BLUE + '--------------------')

while 1 == 1:

    s()
    print()
    print('Сделано пользователем user30402.')
    print()
    s()
    print()
    print('Добро пожаловать в универсальную программу для вычислений, для начала работы выберите пункт.')
    print()
    s()
    print()
    print('1 - Калькулятор; 2 - Вычисление квадратного корня; 3 - Решение квадратных уравнений через дискриминант;')
    print()
    print('4 - Тригонометрия; 5 - Теорема Пифагора; 6 - Калькулятор дробей; 7 - Перевод дробей; 8 - Контакты разработчика.')
    print()
    s()
    print()
    choice = input('Введите номер пункта: ')
    print()
    s()
    print()

    if choice == '1':
        print('Вы выбрали калькулятор.')
        print()
        mathex = input('Введите математический пример через пробелы: ')
        print()
        try:
            num1, sign, num2 = mathex.split(' ')
            num1, sign, num2 = float(num1), sign, float(num2)
            if sign == '+':
                print('Ответ: ' + str(num1 + num2) + '.')
            elif sign == '-':
                print('Ответ: ' + str(num1 - num2) + '.')
            elif sign == '*':
                print('Ответ: ' + str(num1 * num2) + '.')
            elif sign == '/' or sign == ':':
                try:
                    print('Ответ: ' + str(num1 / num2))
                except:
                    print('Невозможно деление на ноль.')
            elif sign == '**' or sign == '^':
                print('Ответ: ' + str(num1 ** num2) + '.')
            else:
                print('Введён неизвестный знак.')
        except:
            print('Ошибка, попробуйте ставить пробелы.')
    elif choice == '2':
        print('Вы выбрали вычисление квадратного корня.')
        print()
        num = int(input('Введите число: '))
        print()
        if num < 0:
            print('Ответ: i')
        elif num == 0 or int(num) > 0:
            print('Ответ: ' + str(math.sqrt(int(num))) + '.')
        else:
            print('Неизвестная ошибка!')

    elif choice == '3':
        print('Вы выбрали решение квадратных уравнений через дискриминант.')
        print()
        mathex = input('Введите a, b, c через запятую: ')
        a, b, c = mathex.split(',')
        a, b, c = float(a), float(b), float(c)
        print()
        D = (b**2) - (4*a*c)
        print('D = b^2 - 4ac = ' + str(D))
        print()
        if D < 0:
            print('Корней нет. ')
        elif D == 0:
            print('1 корень; ')
            print()
            x = -b/2*a
            print('x = -(b / 2a) = ' + str(x) + ';')
            print('Ответ: ' + str(x) + '.')
        elif D > 0:
            print('2 корня.')
            print()
            x1 = -(b - math.sqrt(D)) / (2*a)
            x2 = -(b + math.sqrt(D)) / (2*a)
            print('x1 = -(b - √D) / (2a) = ' + str(x1) + ';')
            print('x2 = -(b + √D) / (2a) = ' + str(x2) + ';')
            print()
            print('Ответ: ' + str(x1) + '; ' + str(x2) + '.')
        else:
            print('Неизвестная ошибка.')
            
    elif choice == '4':
        print('Вы выбрали тригонометрию.')
        print()
        print('Выберите то, что нужно найти.')
        print()
        print('1 - Синус; 2 - Косинус;')
        print()
        choice = input('Введите пункт: ')
        print()
        if choice == '1':
            trx = float(input('Введите косинус: '))
            print()
            if trx > 1:
                print('Косинус не может быть больше единицы!')
            elif trx < -1:
                print('Косинус не может быть меньше минус единицы!')
            else:
                xsinrcos = math.sqrt(1 - trx**2)
                print('Ответ: ' + str(xsinrcos) + '.')
        elif choice == '2':
            trx = float(input('Введите синус: '))
            print()
            if trx > 1:
                print('Синус не может быть больше единицы!')
            elif trx < -1:
                print('Синус не может быть меньше минус единицы!')
            else:
                xsinrcos = math.sqrt(1 - trx**2)
                print('Ответ: ' + str(xsinrcos) + '.')
        else:
            print('Выбран несуществующий пункт.')

    elif choice == '5':
        print('Вы выбрали Теорему Пифагора.')
        print()
        print('Выберите то, что нужно найти.')
        print()
        print('1 - Катет; 2 - Гипотенузу;')
        print()
        korg = input('Введите пункт: ')
        print()
        if korg == '1':
            a = int(input('Введите значение известного катета: '))
            print()
            c = int(input('Введите значение гипотенузы: '))
            b2 = c**2 - a**2
            print()
            if b2 < 0:
                print('Ответ: Решений нет.')
            else:
                b = math.sqrt(b2)
                print('Ответ: ' + str(b) + '.')
        elif korg == '2':
            a = int(input('Введите значение первого катета: '))
            b = int(input('Введите значение второго катета: '))
            c2 = a**2 + b**2
            c = math.sqrt(c2)
            print()
            print('c^2 = ' + str(c2) + ';')
            print()
            print('Ответ: ' + str(c) + '.')
        else:
            print('Выбран несуществующий пункт.')

    elif choice == '6':
        print('Вы выбрали калькулятор дробей.')
        print()
        a = int(input('Введите числитель первой дроби: '))
        b = int(input('Введите знаменатель первой дроби: '))
        print()
        sign = input('Введите знак: ')
        print()
        c = int(input('Введите числитель второй дроби: '))
        d = int(input('Введите знаменатель второй дроби: '))
        print()
        if sign == '+':
            if b == d:
                sac = a + c
                print('Ответ: ' + str(sac) + '/' + str(b) + '.')
            elif b != d:
                bd = b*d
                ad = a*d
                cb = c*b
                adcb = ad+cb
                print('Ответ: ' + str(adcb) + '/' + str(bd) + '.')
            else:
                print('Неизвестная ошибка.')
        elif sign == '-':
            if b == d:
                rac = a - c
                print('Ответ: ' + str(rac) + '/' + str(b) + '.')
            elif b != d:
                rbd = b*d
                rad = a*d
                rcb = c*b
                radcb = rad-rcb
                print('Ответ: ' + str(radcb) + '/' + str(bd) + '.')
            else:
                print('Неизвестная ошибка.')
        elif sign == '*':
            ac = a*c
            bd = b*d
            print('Ответ: ' + str(ac) + '/' + str(bd) + '.')
        elif sign == '/':
            ad = a*d
            bc = b*c
            print('Ответ: ' + str(int(ad)) + '/' + str(int(bc)) + '.')
        else:
            print('Введён неизвестный знак.')
            
    elif choice == '7':
        print('Вы выбрали перевод дробей.')
        print()
        print('Выберите метод перевода.')
        print()
        print('1 - Обыкновенная -> Десятичная.')
        print()
        choice = input('Введите пункт: ')
        print()
        if choice == '1':
            a = int(input('Введите числитель дроби: '))
            b = int(input('Введите знаменатель дроби: '))
            print()
            chab = a/b
            print('Ответ: ' + str(chab) + '.')
        else:
            print('Выбран несуществующий пункт.')

    elif choice == '8':
        print('Вы выбрали контакты разработчика.')
        print()
        yt = 'https://www.youtube.com/channel/UCTRNc1pp445lg8USsC57C-g'
        github = 'https://github.com/user30402'
        vk = 'https://vk.com/user30402'
        print('YouTube - ' + yt)
        print()
        print('GitHub - ' + github)
        print()
        print('VK - ' + vk)

    else:
        print('Выбран несуществущий пункт. ')
    print()
    s()
    print()
    input('Нажмите Enter, чтобы очистить терминал... ')
    os.system('cls')
