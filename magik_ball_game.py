from random import *

answers = [
    "Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова",
    "Даже не думай", "Предрешено", "Вероятнее всего", "Спроси позже",
    "Мой ответ - нет", "Никаких сомнений", "Хорошие перспективы",
    "Лучше не рассказывать", "По моим данным - нет", "Можешь быть уверен в этом",
    "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"
]

print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
name = input("Как вас зовут? ")
print(f"Привет {name}")

while True:
    print(f"Задай свой вопрос, {name}.")
    question = input()
    print(choice(answers))
    one_more = input(
        "Если хотите задать еще вопрос нажмите 'д' - да, 'н' - нет. ")
    if one_more in ('y', 'н'):
        print("Возвращайся если возникнут вопросы!")
        break
