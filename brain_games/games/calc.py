import random
from brain_games.cli import welcome_user


DESCRIPTION = "What is the result of the expression?"
welcome_user_func = welcome_user


def generate_round():
    # Генерирует одно выражение и правильный ответ
    number1 = random.randint(1, 20)
    number2 = random.randint(1, 20)
    operator = random.choice(["+", "-", "*"])

    match operator:
        case "+":
            correct_answer = number1 + number2
        case "-":
            correct_answer = number1 - number2
        case "*":
            correct_answer = number1 * number2

    question = f"{number1} {operator} {number2}"
    return question, str(correct_answer)
