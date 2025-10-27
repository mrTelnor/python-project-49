import prompt


import random


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")

    correct_answers = 0
    rounds_to_win = 3

    while correct_answers < rounds_to_win:
        number1 = random.randint(1, 20)
        number2 = random.randint(1, 20)
        operator = random.choice(["+", "-", "*"])

        # Вычисляем правильный ответ
        if operator == "+":
            correct_answer = number1 + number2
        elif operator == "-":
            correct_answer = number1 - number2
        else:
            correct_answer = number1 * number2

        print(f"Question: {number1} {operator} {number2}")
        answer = prompt.string("Your answer: ").strip()

        # Проверка правильности
        if answer == str(correct_answer):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return  # Завершаем игру при ошибке

    print(f"Congratulations, {name}!")
