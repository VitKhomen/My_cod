from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

n = int(input("Количество паролей для генерации? "))
length = int(input("Каккая должна быть длина пароля? "))
add_digits = input("В пароле должны быть цифры?(да, нет) ")
add_low_lett = input("В пароле должны быть строчные буквы?(да, нет) ")
add_upp_lett = input("В пароле должны быть большие буквы?(даб нет) ")
add_punctuation = input("В пароле должны быть знаки пунктуации?(да, нет) ")
remove_bad_simbol = input(
    "Исключать ли неоднозначные символы il1Lo0O?(да, нет) ")

if add_digits.lower() == 'да':
    chars += digits
if add_low_lett.lower() == 'да':
    chars += lowercase_letters
if add_upp_lett.lower() == 'да':
    chars += uppercase_letters
if add_punctuation.lower() == 'да':
    chars += punctuation
if remove_bad_simbol.lower() == 'да':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')


def generate_password(length, char):
    pasword = ''
    for i in range(length):
        pasword += choice(char)
    return pasword


for j in range(n):
    print(generate_password(length, chars))
