import time
from colorama import init, Fore, Back, Style

def time_txt(sec, text):
    #Оптимизация с помощью ФУЕКЦИЙ X)
    print(text)
    time.sleep(sec)

print("Подождите пока я здесь немного поколдую...")
time.sleep(1)
time_txt(0.7, '3...')
init()
time_txt(0.7, '2...')
time_txt(0.7, '1...')

time_txt(0.7, Fore.CYAN + 'Усё, теперь готово' + Style.RESET_ALL)
print(Fore.GREEN + 'Это программа оценки твоей производительности!', Style.RESET_ALL)
print('Выбери вариант ниже:')

try:
    select = int(input(Fore.BLUE + '1) Использовать программу ' + '\n2) Выйти' + Style.RESET_ALL + Fore.WHITE + ' \n>>>' + Style.RESET_ALL))

    if select == 1:
        print(Fore.WHITE + 'Формула: ' + Back.BLUE + 'для того чтобы программа правильно работала надо ввести - время отработаное ' + Fore.RED  + 'ПО ФАКТУ', Fore.WHITE + ' потом, количество' + Fore.RED + 'ВЫПОЛНЕНЫХ ' + Fore.WHITE + ' и ' + Fore.RED + 'НЕ ВЫПОЛНЕНЫХ' + Fore.WHITE + '. Все!', Style.RESET_ALL)
        print(Back.CYAN, Fore.WHITE + 'Так вот начнем!', Style.RESET_ALL)

        time_text = float(input('Время отработаное, ваше величество:'))
        success_work = float(input('Законченые задания, так-же - ваше величество:'))
        failed_work = float(input(Fore.RED + 'НЕ ' + Style.RESET_ALL + 'Законченые задания, так-же - ваше величество:'))

        print('Сейчас...')
        result = time_text*(success_work - failed_work)

        print('Результат оценки >>>', result)
    elif select == 2:
        time_txt(1, 'Выход...')
        print('Вышли!')
    else:
        print(Fore.RED, 'ОШИБКА: нет такого пункта "' + str(select) + '"', Style.RESET_ALL)
except:
    print(Fore.RED, 'ОШИБКА: попробуйте ввести цифру', Style.RESET_ALL)
