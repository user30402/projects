import math
import os

clear = lambda: os.system('cls')
while 1 == 1:
    print('Добро пожаловать в универсальную программу для вычислений, для начала работы выберите пункт.')
    print()
    print('1 - Калькулятор; 2 - Вычисление квадратного корня; 3 - Решение квадратных уравнений через дискриминант; 4 - Тригонометрия; 5 - Теорема Пифагора.')
    print()
    choice = int(input('Введите номер пункта: '))
    print()
    print('--------------------')
    print()
    if choice == 1:
        print('Вы выбрали калькулятор.')
        print()
        num1 = int(input('Введите число: '))
        sign = str(input('Введите знак: '))
        num2 = int(input('Введите число: '))
        print()
        if sign == '+':
            print('Ответ: ' + str(num1 + num2))
        elif sign == '-':
            print('Ответ: ' + str(num1 - num2))
        elif sign == '*':
            print('Ответ: ' + str(num1 * num2))
        elif sign == '/' or sign == ':':
            print('Ответ: ' + str(num1 / num2))
        elif sign == '**' or sign == '^':
            print('Ответ: ' + str(num1 ** num2))
    elif choice == 2:
        print('Вы выбрали вычисление квадратного корня.')
        print()
        num = int(input('Введите число: '))
        print()
        print('Квадратным корнем числа ' + str(num) + ' является число ' + str(math.sqrt(num)) + '.')
    elif choice == 3:
        print('Вы выбрали решение квадратных уравнений через дискриминант.')
        print()
        a = int(input('Введите a: '))
        b = int(input('Введите b: '))
        c = int(input('Введите c: '))
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
    elif choice == 4:
        print('Вы выбрали тригонометрию.')
        print()
        print('Выберите то, что нужно найти.')
        print()
        print('1 - Синус; 2 - Косинус;')
        print()
        ask = int(input('Введите пункт: '))
        print()
        if ask == 1:
            trx = float(input('Введите косинус: '))
            xsinrcos = math.sqrt(1 - trx**2)
            print()
            print('Ответ: ' + str(xsinrcos) + '.')
        elif ask == 2:
            trx = float(input('Введите синус: '))
            xsinrcos = math.sqrt(1 - trx**2)
            print()
            print('Ответ: ' + str(xsinrcos) + '.')
        else:
            print('Выбран несуществующий пункт.')
    elif choice == 5:
        print('Вы выбрали Теорему Пифагора.')
        print()
        print('Выберите то, что нужно найти.')
        print()
        print('1 - Катет; 2 - Гипотенузу;')
        print()
        korg = int(input('Введите пункт: '))
        print()
        if korg == 1:
            a = int(input('Введите значение известного катета: '))
            print()
            c = int(input('Введите значение гипотенузы: '))
            b2 = gi**2 - k**2
            b = math.sqrt(b2)
            print()
            print('k^2 = ' + str(b2) + ';')
            print()
            print('Ответ: ' + str(b) + '.')
        elif korg == 2:
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
    else:
        print('Выбран несуществущий пункт. ')
    print()
    print('--------------------')
    print()
    input('Нажмите Enter, чтобы очистить терминал... ')
    clear()
