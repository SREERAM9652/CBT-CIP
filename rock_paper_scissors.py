import random

# Define the choices and rules
choices = ["rock", "paper", "scissors"]
rules = {
    "rock": {"rock": "draw", "paper": "lose", "scissors": "win"},
    "paper": {"rock": "win", "paper": "draw", "scissors": "lose"},
    "scissors": {"rock": "lose", "paper": "win", "scissors": "draw"}
}

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_choice not in choices:
        print("Invalid choice. Please choose again.")
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    result = rules[user_choice][computer_choice]
    return result

def main():
    print("Welcome to Rock, Paper, Scissors Game!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        
        if result == "win":
            print("You win!")
        elif result == "lose":
            print("You lose!")
        else:
            print("It's a draw!")
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
