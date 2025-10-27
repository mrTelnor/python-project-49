import random
from brain_games.cli import welcome_user


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
welcome_user_func = welcome_user


def is_even(number: int) -> bool:
    # Проверяет, является ли число чётным
    return number % 2 == 0


def generate_round():
    # Генерирует один вопрос и правильный ответ
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if is_even(number) else "no"
    return question, correct_answer