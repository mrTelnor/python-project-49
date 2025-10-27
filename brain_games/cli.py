import prompt


def welcome_user() -> str:
    # Приветствует пользователя и возвращает его имя
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name