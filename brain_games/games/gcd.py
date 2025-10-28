import random

DESCRIPTION = "Find the greatest common divisor of given numbers."


def calc_gcd(a, b):
    # Вычисляет наибольший общий делитель по алгоритму Евклида
    while b != 0:
        temp = b
        remainder = a % b
        a = temp
        b = remainder
    return a


def generate_round():
    # Генерирует вопрос и правильный ответ
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f"{number1} {number2}"
    correct_answer = str(calc_gcd(number1, number2))
    return question, correct_answer
