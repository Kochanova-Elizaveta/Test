from engine import run_game
from games.lcm_game import lcm_game_logic
from games.geometric_progression_game import geometric_progression_game_logic

def main():
    print("Choose a game:")
    print("1. LCM Game")
    print("2. Geometric Progression Game")
    choice = input().strip()

    if choice == '1':
        run_game(lcm_game_logic, "Find the smallest common multiple of given numbers.")
    elif choice == '2':
        run_game(geometric_progression_game_logic, "What number is missing in the progression?")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
