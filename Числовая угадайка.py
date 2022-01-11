from random import randint
s = randint(1,100)# рандомное число генерируем от 1 до  100

def is_valid(n): #Защита от дурака
    if n in range(1,101):
        return True
    else:
        return False

def repeat():
    word = input('Не хотите сыграть еще раз? ДА/НЕТ:')
    if word == 'да' or word == 'ДА':
        start()
    else:
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        raise SystemExit(1)


def igra():
    counter = 0
    while True:
        n = int(input('Введите число от 1 до 100:'))
        if is_valid(n) == True:
            if n < s:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                counter+=1
            elif n > s:
                print('Ваше число больше загаданного, попробуйте еще разок')
                counter+=1
            elif n == s:
                print('Поздравляем вы угадали число за ',counter,'попыток!')
                repeat()
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
def start():
    print('Добро пожаловать в числовую угадайку')
    igra()
start()
