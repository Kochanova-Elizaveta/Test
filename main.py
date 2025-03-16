import random
import math


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def lcm_game():
    print("Welcome to the Brain Games! May I have your name?")
    name = input()
    print(f"Hello, {name}!")
    print("Find the smallest common multiple of given numbers.")

    score = 0
    for _ in range(3):
        nums = [random.randint(1, 100) for _ in range(3)]
        correct_answer = nums[0]
        for num in nums[1:]:
            correct_answer = lcm(correct_answer, num)

        print(f"Question: {nums[0]} {nums[1]} {nums[2]}")
        user_answer = int(input("Your answer: "))

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"'{user_answer}' is wrong answer. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")

    if score == 3:
        print(f"Congratulations, {name}!")
    else:
        print(f"Game Over, {name}. You got {score} out of 3.")


def geometric_progression_game():
    print("Welcome to the Brain Games! May I have your name?")
    name = input()
    print(f"Hello, {name}!")
    print("Find the missing number in the geometric progression.")

    score = 0
    for _ in range(3):
        length = random.randint(5, 10)
        ratio = random.randint(2, 5)
        start = random.randint(1, 10)
        progression = [start * ratio**i for i in range(length)]
        missing_index = random.randint(0, length - 1)
        hidden_number = progression[missing_index]
        progression[missing_index] = '..'

        print(f"Question: {' '.join(map(str, progression))}")
        user_answer = int(input("Your answer: "))

        if user_answer == hidden_number:
            print("Correct!")
            score += 1
        else:
            print(f"'{user_answer}' is wrong answer. "
                  f"Correct answer was '{hidden_number}'.")
            print(f"Let's try again, {name}!")

    if score == 3:
        print(f"Congratulations, {name}!")
    else:
        print(f"Game Over, {name}. You got {score} out of 3.")


def main():
    print("Choose a game:")
    print("1. LCM Game")
    print("2. Geometric Progression Game")
    choice = input()

    if choice == '1':
        lcm_game()
    elif choice == '2':
        geometric_progression_game()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
