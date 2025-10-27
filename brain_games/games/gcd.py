import random
from math import gcd

DESCRIPTION = "Find the greatest common divisor of given numbers."

def generate_round():
    # Генерирует вопрос и правильный ответ
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f"{number1} {number2}"
    correct_answer = str(gcd(number1, number2))
    return question, correct_answer