import random

items = ["rock", "paper", "scissors"]

def get_computer_choice():
    com_choice = random.choice(items)
    print (f"the computer's choice is: {com_choice}" )
    return com_choice
    
def get_user_choice():
    usr_choice = input("Rock, Paper, Scissors?").lower()
    print (f"you chose : {usr_choice}")
    return usr_choice


while True:
    
    us_choice = get_user_choice()
    co_choice = get_computer_choice()
    if us_choice == co_choice :
        print("It's a tie!")
    elif us_choice == "rock":
        if co_choice == "scissors":
            print("You win!")
        else:
            print("You lose!")
    elif us_choice == "paper":
        if co_choice == "scissors":
            print("You lose!")
        else:
            print("You win!")
    elif us_choice == "scissors":
        if co_choice == "rock":
            print("You lose!")
        else:
            print("You win!")
    
    play_again = input("Play again? (y/n): ")
    if play_again.lower() == "n":
        break
    


