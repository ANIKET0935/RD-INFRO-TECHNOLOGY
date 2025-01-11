import random

def get_computer_choice():
    """Randomly select rock, paper, or scissors for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Main function to play the Rock-Paper-Scissors game."""
    user_score = 0
    computer_score = 0

    while True:
        print("\n--- Rock-Paper-Scissors Game ---")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit")

        try:
            user_input = int(input("Enter your choice (1/2/3/4): "))
            if user_input == 4:
                print("Thanks for playing! Goodbye!")
                print(f"Final Scores: You - {user_score}, Computer - {computer_score}")
                break

            if user_input not in [1, 2, 3]:
                print("Invalid choice. Please select 1, 2, 3, or 4.")
                continue

            user_choice = ["rock", "paper", "scissors"][user_input - 1]
            computer_choice = get_computer_choice()

            print(f"You chose: {user_choice}")
            print(f"Computer chose: {computer_choice}")

            result = determine_winner(user_choice, computer_choice)
            print(result)

            if "You win!" in result:
                user_score += 1
            elif "Computer wins!" in result:
                computer_score += 1

            print(f"Current Scores: You - {user_score}, Computer - {computer_score}")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    play_game()
