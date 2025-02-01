import random

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You won!!"
    else:
        return "You lose!!"

# Main function to run the game
def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        print("\n--- Rock, Paper, Scissors ---")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")
        
        # Get user choice
        user_choice = input("Choose (1/2/3): ")
        
        if user_choice == "1":
            user_choice = "rock"
        elif user_choice == "2":
            user_choice = "paper"
        elif user_choice == "3":
            user_choice = "scissors"
        elif user_choice == "4":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")
            continue
        
        # Get computer choice
        computer_choice = get_computer_choice()
        
        # Display the choices
        print(f"\nYou chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")
        
        # Determine the winner and display the result
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        # Update score based on the result
        if result == "You won!!":
            user_score += 1
        elif result == "You lose!!":
            computer_score += 1
        
        # Display the current scores
        print(f"Your score: {user_score}")
        print(f"Computer's score: {computer_score}")
        
        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Byebye!!")
            break

# Start the game
if __name__ == "__main__":
    play_game()
