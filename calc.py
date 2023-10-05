import math
import os
import time

clear = lambda: os.system('cls')
sin = math.sin
cos = math.cos

while True:
    print('Добро пожаловать в универсальную программу для вычислений, для начала работы выберите пункт.')
    print()
    print('1 - Калькулятор; 2 - Вычисление квадратного корня; 3 - Решение квадратных уравнений через дискриминант; 4 - Тригонометрия.')
    print()
    choice = int(input('Введите номер пункта: '))
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
        print('D = b^2 - 4ac.')
        print()
        D = (b**2) - (4 * a * c)
        if D < 0:
            print('Корней нет. ')
        elif D == 0:
            print('1 корень. ')
            print()
            print('x = -(b / 2a)')
            x = -b / 2 * a
            print('Ответ: ' + str(x) + '.')
        elif D > 0:
            print('2 корня.')
            print()
            print('x1 = -(b - √D) / (2a)')
            print('x2 = -(b + √D) / (2a)')
            x1 = -(b - math.sqrt(D)) / (2*a)
            x2 = -(b + math.sqrt(D)) / (2*a)
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
        print('Выбран несуществущий пункт. ')
    print()
    print('Подождите 5 секунд для очистки терминала... ')
    time.sleep(5)
    clear()
