import math, os, webbrowser as wb, winsound
from colorama import *

def s():
    print(Style.BRIGHT + Fore.BLUE + '--------------------')
    
def snd():
    winsound.PlaySound("*", winsound.SND_ASYNC)

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
    print('4 - Тригонометрия; 5 - Теорема Пифагора; 6 - Калькулятор дробей; 7 - Перевод дробей; 8 - Нахождение площади.')
    print()
    print('9 - Контакты разработчика.')
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
                print(f'Ответ: {num1 + num2}.')
            elif sign == '-':
                print(f'Ответ: {num1 - num2}.')
            elif sign == '*':
                print(f'Ответ: {num1 * num2}.')
            elif sign == '/' or sign == ':':
                try:
                    print(f'Ответ: {num1 / num2}.')
                except:
                    snd()
                    print('Невозможно деление на ноль.')
            elif sign == '**' or sign == '^':
                print(f'Ответ: {num1**num2}.')
            else:
                print('Введён неизвестный знак.')
        except:
            snd()
            print('Ошибка, попробуйте ставить пробелы.')
            
    elif choice == '2':
        print('Вы выбрали вычисление квадратного корня.')
        print()
        num = int(input('Введите число: '))
        print()
        if num < 0:
            print('Ответ: i')
        elif num == 0 or int(num) > 0:
            print(f'Ответ: {math.sqrt(num)}.')
        else:
            snd()
            print('Неизвестная ошибка!')

    elif choice == '3':
        print('Вы выбрали решение квадратных уравнений через дискриминант.')
        print()
        mathex = input('Введите a, b, c через запятую: ')
        a, b, c = mathex.split(',')
        a, b, c = float(a), float(b), float(c)
        print()
        D = (b**2) - (4*a*c)
        print(f'D = b^2 - 4ac = {D}.')
        print()
        if D < 0:
            print('Корней нет. ')
        elif D == 0:
            print('1 корень; ')
            print()
            x = (-b)/(2*a)
            print(f'x = -(b / 2a) = {x};')
            print(f'Ответ: {x}.')
        elif D > 0:
            print('2 корня.')
            print()
            x1 = -(b - math.sqrt(D)) / (2*a)
            x2 = -(b + math.sqrt(D)) / (2*a)
            print(f'x1 = -(b - √D) / (2a) = {x1};')
            print(f'x2 = -(b + √D) / (2a) = {x2};')
            print()
            print(f'Ответ: {x1}; {x2}.')
        else:
            snd()
            print('Неизвестная ошибка.')
            
    elif choice == '4':
        print('Вы выбрали тригонометрию.')
        print()
        print('Выберите то, что нужно найти.')
        print()
        print('1 - Синус; 2 - Косинус;')
        print()
        choice = input('Введите номер пункта: ')
        print()
        if choice == '1':
            trx = float(input('Введите косинус: '))
            print()
            if trx > 1:
                snd()
                print('Косинус не может быть больше единицы!')
            elif trx < -1:
                snd()
                print('Косинус не может быть меньше минус единицы!')
            else:
                xsinrcos = math.sqrt(1 - trx**2)
                print(f'Ответ: {xsinrcos}.')
        elif choice == '2':
            trx = float(input('Введите синус: '))
            print()
            if trx > 1:
                snd()
                print('Синус не может быть больше единицы!')
            elif trx < -1:
                snd()
                print('Синус не может быть меньше минус единицы!')
            else:
                xsinrcos = math.sqrt(1 - trx**2)
                print(f'Ответ: {xsinrcos}.')
        else:
            snd()
            print('Выбран несуществующий пункт.')

    elif choice == '5':
        print('Вы выбрали Теорему Пифагора.')
        print()
        print('Выберите то, что нужно найти.')
        print()
        print('1 - Катет; 2 - Гипотенузу;')
        print()
        choice = input('Введите номер пункта: ')
        print()
        if choice == '1':
            a = int(input('Введите значение известного катета: '))
            print()
            c = int(input('Введите значение гипотенузы: '))
            b2 = c**2 - a**2
            print()
            if b2 < 0:
                print('Ответ: Решений нет.')
            else:
                b = math.sqrt(b2)
                print(f'Ответ: {b}.')
        elif choice == '2':
            a = int(input('Введите значение первого катета: '))
            print()
            b = int(input('Введите значение второго катета: '))
            c2 = a**2 + b**2
            c = math.sqrt(c2)
            print()
            print(f'c^2 = {c2};')
            print()
            print(f'Ответ: {c}.')
        else:
            snd()
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
                print(f'Ответ: {sac}/{b}.')
            elif b != d:
                bd = b*d
                ad = a*d
                cb = c*b
                adcb = ad+cb
                print(f'Ответ: {adcb}/{bd}.')
            else:
                snd()
                print('Неизвестная ошибка.')
        elif sign == '-':
            if b == d:
                rac = a - c
                print(f'Ответ: {rac}/{b}.')
            elif b != d:
                rbd = b*d
                rad = a*d
                rcb = c*b
                radcb = rad-rcb
                print(f'Ответ: {radcb}/{bd}.')
            else:
                snd()
                print('Неизвестная ошибка.')
        elif sign == '*':
            ac = a*c
            bd = b*d
            print(f'Ответ: {ac}/{bd}.')
        elif sign == '/':
            ad = a*d
            bc = b*c
            print(f'Ответ: {ad}/{bc}.')
        else:
            snd()
            print('Введён неизвестный знак.')
            
    elif choice == '7':
        print('Вы выбрали перевод дробей.')
        print()
        print('Выберите метод перевода.')
        print()
        print('1 - Обыкновенная -> Десятичная.')
        print()
        choice = input('Введите номер пункта: ')
        print()
        if choice == '1':
            a = int(input('Введите числитель дроби: '))
            b = int(input('Введите знаменатель дроби: '))
            print()
            chab = a/b
            print(f'Ответ: {chab}.')
        else:
            snd()
            print('Выбран несуществующий пункт.')

    elif choice == '8':
        print('Вы выбрали нахождение площади.')
        print()
        print('1 - Площадь квадрата; 2 - Площадь прямоугольника; 3 - Площадь прямоугольного треугольника; 4 - Площадь круга; 5 - Площадь трапеции.')
        print()
        choice = input('Введите номер пункта: ')
        print()
        if choice == '1':
            print('Вы выбрали нахождение площади квадрата.')
            print()
            print('1 - Нахождение площади по стороне; 2 - Нахождение площади по диагонали.')
            print()
            choice = input('Введите номер пункта: ')
            print()
            if choice == '1':
                print('Вы выбрали нахождение площади квадрата по стороне.')
                print()
                a = int(input('Введите сторону квадрата: '))
                print()
                a = a**2
                print(f'Ответ: {a}.')
            elif choice == '2':
                print('Вы выбрали нахождение площади квадрата по диагонали.')
                print()
                d = int(input('Введите диагональ квадрата: '))
                print()
                d = (d ** 2) / (2)
                print(f'Ответ: {d}.')
            else:
                snd()
                print('Выбран несуществующий пункт.')
        elif choice == '2':
            print('Вы выбрали нахождение площади прямоугольника.')
            print()
            a = input('Введите две стороны прямоугольника через запятую: ')
            print()
            a, b = a.split(',')
            a, b = float(a), float(b)
            print()
            ab = a * b
            print(f'Ответ: {ab}')
        elif choice == '3':
            print('Вы выбрали нахождение площади прямоугольного треугольника.')
            print()
            a = input('Введите 2 катета треугольника через запятую ')
            k1, k2 = a.split(',')
            k1, k2 = float(k1), float(k2)
            a = (k1 * k2) / (2)
            print()
            print(f'Ответ: {a}.')
        elif choice == '4':
            print('Вы выбрали нахождение площади круга.')
            print()
            a = float(input('Введите радиус круга: '))
            a = (a ** 2) * math.pi
            print()
            print(f'Ответ: {a}.')
        elif choice == '5':
            print('Вы выбрали нахождение площади трапеции.')
            print()
            a = input('Введите два основания трапеции через запятую: ')
            a, b = a.split(',')
            a, b = float(a), float(b)
            h = float(input('Введите высоту трапеции: '))
            st = ((a + b) / 2) * (h)
            print()
            print(f'Ответ: {st}.')
        else:
            snd()
            print('Выбран несуществующий пункт.')

    elif choice == '9':
        print('Вы выбрали контакты разработчика.')
        print()
        yt = 'https://www.youtube.com/channel/UCTRNc1pp445lg8USsC57C-g'
        github = 'https://github.com/user30402'
        vk = 'https://vk.com/user30402'
        print(f'YouTube - {yt}')
        print()
        print(f'GitHub - {github}')
        print()
        print(f'VK - {vk}')

    else:
        snd()
        print('Выбран несуществущий пункт. ')
    print()
    s()
    print()
    input(Style.BRIGHT + Fore.RED + 'Нажмите Enter, чтобы очистить консоль... ')
    os.system('cls')
