from random import *


def begin_gess_game():
    print("Добро пожаловать в числовую угадайку")
    print("Я загадал число от 1 до 100 попробуй отгадать")
    gess_game()


def is_valid(num):
    return num.isdigit() and int(num) in range(1, 101)


def gess_game():
    required_num = randint(1, 101)
    cuonter_gess = 0
    while True:
        cuonter_gess += 1
        input_num = input("Введите число от 1 до 100: ")
        if not is_valid(input_num):
            print("А может быть все-таки введем целое число от 1 до 100?")
            continue
        input_num = int(input_num)

        if required_num < input_num:
            print("Ваше число больше загаданного, попробуйте еще разок")
        elif required_num > input_num:
            print("Ваше число меньше загаданного, попробуйте еще разок")
        else:
            print(f"Поздравляем вы угадали число с {cuonter_gess} попытки")
            one_more = input("Если хотите сыграть еще раз введите 'ДА': ")
            if one_more in ['ДА', 'LF', 'lf', 'да']:
                gess_game()
            else:
                print("Ну ладно")
                break


begin_gess_game()
