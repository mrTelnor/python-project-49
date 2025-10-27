from brain_games.cli import welcome_user


def main():
    welcome_user()


if __name__ == '__main__':
    main()

#import prompt
#
#from brain_games.cli import welcome_user
#from brain_games.engine import run_game
#from brain_games.games import calc, even, gcd, prime, progression
#
#
#def main():
#    name = welcome_user()
#
#    while True:
#        print("\nChoose a game:")
#        print("1 - Calc (калькулятор)")
#        print("2 - Even (проверка на чётность)")
#        print("3 - GCD (наибольший общий делитель)")
#        print("4 - Prime (простое ли число?)")
#        print("5 - Progression (арифметическая прогрессия)")
#        print("0 - Exit")
#
#        choice = prompt.string("Your choice: ").strip()
#
#        match choice:
#            case "1":
#                run_game(calc, name)
#            case "2":
#                run_game(even, name)
#            case "3":
#                run_game(gcd, name)
#            case "4":
#                run_game(prime, name)
#            case "5":
#                run_game(progression, name)
#            case "0":
#                print(f"Goodbye, {name}!")
#                break
#            case _:
#                print("Unknown choice. Please select 1 - 3 or 0.")
#
#
#if __name__ == "__main__":
#    try:
#        main()
#    except KeyboardInterrupt:
#        print("\nGame interrupted. Goodbye!")