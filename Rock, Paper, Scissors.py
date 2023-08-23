import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    computer_choice = random.choice(choices)
    
    print(f"Computer chose: {computer_choice}")
    
    if user_choice in choices:
        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == "rock":
            if computer_choice == "paper":
                print("Computer wins!")
            else:
                print("You win!")
        elif user_choice == "paper":
            if computer_choice == "scissors":
                print("Computer wins!")
            else:
                print("You win!")
        elif user_choice == "scissors":
            if computer_choice == "rock":
                print("Computer wins!")
            else:
                print("You win!")
    else:
        print("Invalid choice. Please choose rock, paper, or scissors.")

rock_paper_scissors()
