import random

def get_user_choice():
    while True:
        user_choice = input("Choose (rock/paper/scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        print("Invalid choice! Try again.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie! 🤝"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win! 🎉"
    else:
        return "Computer wins! 🤖"

def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        print("\n--- Rock Paper Scissors ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if "win" in result:
            user_score += 1
        elif "Computer" in result:
            computer_score += 1
        
        print(f"\nScore: You {user_score} - {computer_score} Computer")
        
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != "y":
            print("\nThanks for playing! 👋")
            break

if __name__ == "__main__":
    play_game()