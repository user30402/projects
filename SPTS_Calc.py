import os, time
from colorama import *

def clear(x):
    time.sleep(x)
    os.system('cls')

def welcome():
    print(Style.BRIGHT + Fore.GREEN + 'Made')
    clear(1)
    print('Made by')
    clear(1)
    print('Made by user30402')
    time.sleep(1.5)
    clear(0.1)
    print('Made by user3040')
    clear(0.1)
    print('Made by user304')
    clear(0.1)
    print('Made by user30')
    clear(0.1)
    print('Made by user3')
    clear(0.1)
    print('Made by user')
    clear(0.1)
    print('Made by use')
    clear(0.1)
    print('Made by us')
    clear(0.1)
    print('Made by u')
    clear(0.1)
    print('Made by ')
    clear(0.1)
    print('Made b')
    clear(0.1)
    print('Made ')
    clear(0.1)
    print('Mad')
    clear(0.1)
    print('Ma')
    clear(0.1)
    print('M')
    clear(0.1)
    time.sleep(1)
    print('|-------------------------|')
    clear(0.1)
    print('|-------------------------| \n')
    clear(0.1)
    print('|-------------------------| \n \nMade by user30402')
    clear(0.1)
    print('|-------------------------| \n \nMade by user30402 \n \n|-------------------------|')
    clear(0.1)
    print('|-------------------------| \n \nMade by user30402 \n \n|-------------------------| \n \n1 - Calculate stats over time; 2 - Calculate time for stat; 3 - Stats for the location')
    clear(0.1)
    print('|-------------------------| \n \nMade by user30402 \n \n|-------------------------| \n \n1 - Calculate stats over time; 2 - Calculate time for stat; 3 - Stats for the location \n \n|-------------------------|')
    clear(0.1)
    print('|-------------------------| \n \nMade by user30402 \n \n|-------------------------| \n \n1 - Calculate stats over time; 2 - Calculate time for stat; 3 - Stats for the location \n \n|-------------------------| \n ')
    clear(0.1)

def main():
    def mult0(getstat, getmult):
        if getmult == 'U' or getmult == 'u':
            getstat *= 1
        elif getmult == 'K' or getmult == 'k':
            getstat *= 1000
        elif getmult == 'M' or getmult == 'm':
            getstat *= 1000000
        elif getmult == 'B' or getmult == 'b':
            getstat *= 1000000000
        elif getmult == 'T' or getmult == 't':
            getstat *= 1000000000000
        elif getmult == 'Qa' or getmult == 'qa':
            getstat *= 1000000000000000
        elif getmult == 'Qi' or getmult == 'qi':
            getstat *= 1000000000000000000
        elif getmult == 'Sx' or getmult == 'sx':
            getstat *= 1000000000000000000000
        elif getmult == 'Sp' or getmult == 'sp':
            getstat *= 1000000000000000000000000
        elif getmult == 'Oc' or getmult == 'oc':
            getstat *= 1000000000000000000000000000
        elif getmult == 'No' or getmult == 'no':
            getstat *= 1000000000000000000000000000000
        elif getmult == 'Ud' or getmult == 'ud':
            getstat *= 1000000000000000000000000000000000
        elif getmult == 'Dd' or getmult == 'dd':
            getstat *= 1000000000000000000000000000000000000
        elif getmult == 'Td' or getmult == 'td':
            getstat *= 1000000000000000000000000000000000000000

        return getstat
    
    def resmult0(getresmult, getmult):
        if getresmult == 0:
            getmult = 'U'
        elif getresmult == 1:
            getmult = 'K'
        elif getresmult == 2:
            getmult = 'M'
        elif getresmult == 3:
            getmult = 'B'
        elif getresmult == 4:
            getmult = 'T'
        elif getresmult == 5:
            getmult = 'Qa'
        elif getresmult == 6:
            getmult = 'Qi'
        elif getresmult == 7:
            getmult = 'Sx'
        elif getresmult == 8:
            getmult = 'Sp'
        elif getresmult == 9:
            getmult = 'Oc'
        elif getresmult == 10:
            getmult = 'No'
        elif getresmult == 11:
            getmult = 'Ud'
        elif getresmult == 12:
            getmult = 'Dd'
        elif getresmult == 13:
            getmult = 'Td'
        else:
            getmult = '???'

        return getmult
    
    def decoration():
        print(Style.BRIGHT + Fore.GREEN + '|-------------------------|')

    def result0(getstat, getresmult):
        while getstat >= 1000:
            getstat /= 1000
            getresmult += 1

        return getstat, getresmult

    def choice1():
        resmult = 0
        print()
        print(Fore.CYAN + 'You have chosen to calculate stats over time')
        print(Fore.GREEN)
        stat = float(input('Enter the amount of stat per tick: '))
        print()
        statmult = input('Enter the stat multiplier (U; K; M; B; T; Qa; Qi; Sx; Sp; Oc; No; Ud; Dd; Td): ')
        stat = mult0(stat, statmult)
        print()
        delay = float(input('Enter the interval between stat gains (0.5; 1; 1.5): '))

        if delay == 0.5:
            stat *= 2
        elif delay == 1:
            stat *= 1
        elif delay == 1.5:
            stat *= 0.8

        print()
        afktime = float(input('Enter your AFK time: '))
        print()
        timemult = input('Enter the time multiplier (M; H; D): ')

        if timemult == 'M' or timemult == 'm':
            afktime *= 60
        elif timemult == 'H' or timemult == 'h':
            afktime *= (60 * 60)
        elif timemult == 'D' or timemult == 'd':
            afktime *= (60 * 60 * 24)

        stat *= afktime

        stat, resmult = result0(stat, resmult)

        statmult = resmult0(resmult, statmult)
        stat = round(stat, 2)
        
        print()
        print(Fore.YELLOW + f'You will receive +{stat}{statmult} stat.')
    
    def choice2():
        resmult = 0
        print()
        print(Fore.CYAN + 'You have chosen to calculate time for stat')
        print()
        xstat = float(input('Enter the amount of stat you need: '))
        print()
        xstatmult = input('Enter the stat multiplier (U; K; M; B; T; Qa; Qi; Sx; Sp; Oc; No; Ud; Dd; Td): ')
        xstat = mult0(xstat, xstatmult)
        print()
        currentstat = float(input('Enter the amount of stat you recieving per tick: '))
        print()
        currentstatmult = input('Enter the stat multiplier (U; K; M; B; T; Qa; Qi; Sx; Sp; Oc; No; Ud; Dd; Td): ')

        currentstat =  mult0(currentstat, currentstatmult)
        currentstatperhour = currentstat * 60 * 60
        timeresult =  xstat / currentstatperhour
        timeresult = round(timeresult, 2)

        xstat, resmult = result0(xstat, resmult)

        xstatmult = resmult0(resmult, xstatmult)
        print()
        print(f'You need {timeresult} hours to farm {xstat}{xstatmult} stat.')

    def choice3():
        resmult = 0
        mult = 0
        print()
        print(Fore.CYAN + 'You have chosen the stats for the location.')
        print(Fore.GREEN)
        print('1 - FS; 2 - BT; 3 - MS/JF; 4 - PP')
        print()
        choice = input('Select the point: ')
        
        if choice == '1':
            print()
            print(Fore.CYAN + 'You have chosen FS locations.')
            print(Fore.GREEN)
            multiplier = int(input('Enter your FS multiplier: '))
            print()
            print('1 - Rock; 2 - Crystal; 3 - Blue Star; 4 - Green Star; 5 - Red Star;')
            print()
            choice = input('Select the point: ')
            print()

            if choice == '1':
                multiplier *= 10
            elif choice == '2':
                multiplier *= 100
            elif choice == '3':
                multiplier *= 2000
            elif choice == '4':
                multiplier *= 40000
            elif choice == '5':
                multiplier *= 800000

        elif choice == '2':
            print()
            print(Fore.CYAN + 'You have chosen BT locations.')
            print(Fore.GREEN)
            multiplier = int(input('Enter your BT multiplier: '))
            print()
            print('1 - Ice Bath; 2 - Fire Bath; 3 - Iceberg; 4 - Tornado; 5 - Volcano; 6 - Hellfire Pit; 7 - Green Acid; 8 - Red Acid')
            print()
            choice = input('Select the point: ')
            print()

            if choice == '1':
                multiplier *= 5
            elif choice == '2':
                multiplier *= 10
            elif choice == '3':
                multiplier *= 20
            elif choice == '4':
                multiplier *= 50
            elif choice == '5':
                multiplier *= 100
            elif choice == '6':
                multiplier *= 2000
            elif choice == '7':
                multiplier *= 40000
            elif choice == '8':
                multiplier *= 800000

        elif choice == '3':
            print()
            print(Fore.CYAN + 'You have chosen MS/JF locations.')
            print(Fore.GREEN)
            multiplier = int(input('Enter your MS/JF multiplier: '))
            print()
            print('1 - 100 LB; 2 - 1 Ton; 3 - 10 Ton; 4 - 100 Ton; 5 - 1K Ton; 6 - 10K Ton; 7 - 100K Ton; 8 - 1M Ton; 9 - 10M Ton; 10 - 1B Ton')
            print()
            choice = input('Select the point: ')
            print()

            if choice == '1':
                multiplier *= 2
            elif choice == '2':
                multiplier *= 5
            elif choice == '3':
                multiplier *= 10
            elif choice == '4':
                multiplier *= 20
            elif choice == '5':
                multiplier *= 150
            elif choice == '6':
                multiplier *= 750
            elif choice == '7':
                multiplier *= 3500
            elif choice == '8':
                multiplier *= 18000
            elif choice == '9':
                multiplier *= 90000
            elif choice == '10':
                multiplier *= 400000

        elif choice == '4':
            print()
            print(Fore.CYAN + 'You have chosen PP locations.')
            print(Fore.GREEN)
            multiplier = int(input('Enter your PP multiplier: '))
            print()
            print("1 - 1M PP; 2 - 1B PP; 3 - 1T PP; 4 - 1Qa PP; 5 - Gaia's Spring")
            print()
            choice = input('Select the point: ')
            print()

            if choice == '1':
                multiplier *= 100
            elif choice == '2':
                multiplier *= 10000
            elif choice == '3':
                multiplier *= 1000000
            elif choice == '4':
                multiplier *= 100000000
            elif choice == '5':
                multiplier *= 2500000000

        multiplier, resmult = result0(multiplier, resmult)

        mult = resmult0(resmult, mult)

        print(f'You will recieve {multiplier}{mult} per tick.')

    try:
        decoration()
        print()
        print('Made by user30402 ')
        print()
        decoration()
        print()
        print('1 - Calculate stats over time; 2 - Calculate time for stat; 3 - Stats for the location')
        print()
        decoration()
        print()
        choice = input('Select the point: ')
        if choice == '1':
            print()
            decoration()
            choice1()
        elif choice == '2':
            print()
            decoration()
            choice2()
        elif choice == '3':
            print()
            decoration()
            choice3()
    except:
        print()
        print(Style.BRIGHT + Fore.RED + 'Unexpected error!')
    print()
    decoration()

    print(Fore.GREEN)
    input('Press Enter to clear the console... ')
    os.system('cls')

    main()

if __name__ == '__main__':
    welcome()
    main()
else:
    print(Style.BRIGHT + Fore.RED + 'Error!')