# объявление функции
# -*- coding: utf-8 -*-
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

s = []
print('Введите свой текст:')
n = input().split(' ')

for i in range(len(n)):
    counter = 0
    w=''
    for c in range(len(n[i])):
        if n[i][c].isalpha():
            counter+=1
    k = counter
    for g in range(len(n[i])):
        if n[i][g] == ' ':
            w=w+' '
        elif n[i][g].isupper():
            x = eng_upper_alphabet.find(n[i][g])
            w=w+eng_upper_alphabet[(x + k) % 26]
        elif n[i][g] == ',':
            w =w+','
        elif n[i][g] == '.':
            w =w+'.'
        elif n[i][g] == '!':
            w = w +'!'
        elif n[i][g] == '"':
            w =w+'"'
        else:
            x = eng_lower_alphabet.find(n[i][g])
            w=w+eng_lower_alphabet[(x + k) % 26]
    n[i] = w
print(*n)