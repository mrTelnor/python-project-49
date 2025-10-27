import prompt

from brain_games.cli import welcome_user

ROUNDS_TO_WIN = 3


def run_game(game, name=None):
    if name is None:
        name = welcome_user()    

    print(game.DESCRIPTION)

    correct_answers_count = 0

    while correct_answers_count < ROUNDS_TO_WIN:
        question, correct_answer = game.generate_round()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ").strip()

        if user_answer == str(correct_answer):
            print("Correct!")
            correct_answers_count += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")