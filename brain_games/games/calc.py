import random


DESCRIPTION = "What is the result of the expression?"


def generate_round():
    # Генерирует выражение и правильный ответ
    number1 = random.randint(1, 20)
    number2 = random.randint(1, 20)
    operator = random.choice(["+", "-", "*"])
    
    # Для вычитания делаем так, чтобы результат всегда был >= 0
    if operator == "-":
        if number2 > number1:
            number1, number2 = number2, number1

    match operator:
        case "+":
            correct_answer = number1 + number2
        case "-":
            correct_answer = number1 - number2
        case "*":
            correct_answer = number1 * number2

    question = f"{number1} {operator} {number2}"
    return question, str(correct_answer)