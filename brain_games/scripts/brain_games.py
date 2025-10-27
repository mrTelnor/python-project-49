import prompt
from brain_games.cli import welcome_user


def main():
    name = welcome_user()

    while True:
        print("\nChoose a game:")
        print("1 - Even (проверка на чётность)")
        print("2 - Calc (математические выражения)")
        print("0 - Exit")

        choice = prompt.string("Your choice: ").strip()

        match choice:
            case "1":
                from brain_games.games import even
                even.run(name)
            case "2":
                from brain_games.games import calc
                calc.run(name)
            case "0":
                print(f"Goodbye, {name}!")
                break
            case _:
                print("Unknown choice. Please select 1, 2 or 0.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye!")