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
    select = int(input(Fore.BLUE + '1) Использовать программу \n2) Настройки' + '\n3) Выйти' + Style.RESET_ALL + Fore.WHITE + ' \n>>>' + Style.RESET_ALL))
    print(Fore.RED, 'ОШИБКА: нет такого пункта "' + select + ')' + '"', Style.RESET_ALL)

    if select == 1:
        print('yed')
    else:
        print(Fore.RED, 'ОШИБКА: нет такого пункта "' + select + ')' + '"', Style.RESET_ALL)
except:
    print(Fore.RED, 'ОШИБКА: попробуйте ввести цифру', Style.RESET_ALL)
