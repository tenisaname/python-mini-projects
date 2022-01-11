# -*- coding: utf-8 -*-
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
s = []

def end():
    print('Хотите еще что-то сделать?да/нет')
    o = input()
    if o == 'да':
        start()
    else:
        pass

def shifr_ru():
    print('Введите свой текст:')
    n = input()
    for i in range(len(n)):
        if n[i] == ' ':
            s.append(' ')
        elif n[i].isupper():
            x = rus_upper_alphabet.find(n[i])
            s.append(rus_upper_alphabet[(x+k)%32])
        elif n[i] == ',':
            s.append(',')
        elif n[i] == '.':
            s.append('.')
        elif n[i] == '!':
            s.append('!')
        else:
            x = rus_lower_alphabet.find(n[i])
            s.append(rus_lower_alphabet[(x+k)%32])
    w = ''
    for i in s:
        w +=i
    print(w)
    end()

def shifr_en():
    print('Введите свой текст:')
    n = input()
    for i in range(len(n)):
        if n[i] == ' ':
            s.append(' ')
        elif n[i].isupper():
            x = eng_upper_alphabet.find(n[i])
            s.append(eng_upper_alphabet[(x+k)%26])
        elif n[i] == ',':
            s.append(',')
        elif n[i] == '.':
            s.append('.')
        elif n[i] == '!':
            s.append('!')
        else:
            x = eng_lower_alphabet.find(n[i])
            s.append(eng_lower_alphabet[(x+k)%26])
    w = ''
    for i in s:
        w +=i
    print(w)
    end()

def de_shifr_en():
    print('Введите свой текст:')
    n = input()
    for i in range(len(n)):
        if n[i] == ' ':
            s.append(' ')
        elif n[i].isupper():
            y = eng_upper_alphabet.find(n[i])
            s.append(eng_upper_alphabet[(y - k) % 26])
        elif n[i] == ',':
            s.append(',')
        elif n[i] == '.':
            s.append('.')
        elif n[i] == '!':
            s.append('!')
        else:
            y = eng_lower_alphabet.find(n[i])
            s.append(eng_lower_alphabet[(y - k) % 26])
    w = ''
    for i in s:
        w += i
    print(w)
    end()

def de_shifr_ru():
    print('Введите свой текст:')
    n = input()
    for i in range(len(n)):
        if n[i] == ' ':
            s.append(' ')
        elif n[i].isupper():
            y = rus_upper_alphabet.find(n[i])
            s.append(rus_upper_alphabet[(y - k) % 32])
        elif n[i] == ',':
            s.append(',')
        elif n[i] == '!':
            s.append('!')
        elif n[i] == '.':
            s.append('.')
        else:
            y = rus_lower_alphabet.find(n[i])
            s.append(rus_lower_alphabet[(y - k) % 32])
    w = ''
    for i in s:
        w += i
    print(w)
    end()

def start():
    print('Здравствуйте,я программа для шифрования и дешифрования при помощи шифра цезаря')
    print('Приступим')
    print('Что будем делать шифровать или дешифровать?sh/de')
    action = input()
    print('На каком языке русский или английский?ru/en')
    lang = input()
    print('Сдвиг')
    global k
    k = int(input())
    if action == 'sh' and lang =='en':
        shifr_en()
    elif action =='sh' and lang =='ru':
        shifr_ru()
    elif action =='de' and lang =='en':
        de_shifr_en()
    elif action == 'de' and lang == 'ru':
        de_shifr_ru()

start()


