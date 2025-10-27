import random

DESCRIPTION = "What number is missing in the progression?"


PROGRESSION_LENGTH_MIN = 5
PROGRESSION_LENGTH_MAX = 10


def generate_progression(length, start, step):
    # Создаёт арифметическую прогрессию заданной длины
    return [start + i * step for i in range(length)]


def generate_round():
    # Генерирует вопрос и правильный ответ
    length = random.randint(PROGRESSION_LENGTH_MIN, PROGRESSION_LENGTH_MAX)
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    progression = generate_progression(length, start, step)

    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."

    question = " ".join(str(num) for num in progression)
    return question, correct_answer
