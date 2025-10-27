import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number: int) -> bool:
    # Проверяет, является ли число чётным
    return number % 2 == 0


def generate_round():
    # Генерирует вопрос и правильный ответ
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if is_even(number) else "no"
    return question, correct_answer