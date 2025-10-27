import random
from brain_games.cli import welcome_user

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


MIN_NUMBER = 1
MAX_NUMBER = 500


def is_prime(number: int) -> bool:
    # Проверяет, является ли число простым
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_round():
    # Генерирует вопрос и правильный ответ
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = "yes" if is_prime(number) else "no"
    question = str(number)
    return question, correct_answer