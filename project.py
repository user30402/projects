import time
import webbrowser
sleep = time.sleep

print('1 - Учёба; 2 - Игры; 3 - Отдых. ')
print()
choice = int(input('Введите пункт: '))

if choice == 1:
    sleep(1)
    webbrowser.open_new_tab('https://gdz.ru/')
    sleep(0.5)
    webbrowser.open_new('https://www.youtube.com/')
    sleep(0.5)
    webbrowser.open_new('https://skysmart.ru/')
    print()
    print('Желаем Вам продуктивной учёбы!')

elif choice == 2:
    sleep(1)
    webbrowser.open('https://vk.com/music/playlist/438779045_51_72ed0060348f6545df')
    print()
    print('Желаем Вам побед!')

elif choice == 3:
    sleep(1)
    webbrowser.open_new('https://www.youtube.com')
    sleep(0.5)
    webbrowser.open_new('https://www.vk.com')
    sleep(0.5)
    webbrowser.open_new('https://www.jut.su')
    print()
    print('Желаем Вам приятного отдыха!')
else:
    print()
    print('Выбранного Вами пункта не существует. Пожалуйста, перезапустите программу и выберите другой пункт.')

print()

input('Нажмите Enter для выхода... ')