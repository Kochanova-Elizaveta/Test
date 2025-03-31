def run_game(game_logic, conditions):
    print("Welcome to the Brain Games!")
    print("May I have your name?", end=" ")
    name = input()
    print(f"Hello, {name}!")
    print(conditions)

    rounds = 3

    for _ in range(rounds):
        question, correct_answer = game_logic()
        print(f"Question: {question}")
        print("Your answer:", end=" ")
        user_answer = input().strip()

        if user_answer == str(correct_answer):
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
