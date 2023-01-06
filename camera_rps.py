import cv2
from keras.models import load_model
import numpy as np
import random
import time

items = ["rock", "paper", "scissors"]
# Import model
model = load_model('keras_model.h5', compile= False)
# Store video capture
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# returns model predictions as a list
def rps_model():
    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image (what that mean?!)
        data[0] = normalized_image
        prediction = model.predict(data)
        # Shows the frame
        cv2.imshow('frame', frame)
        print("Rock, Paper, Scissors?")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)

        return prediction

# Gets the user_choice, calls the rps_model() function
def get_user_choice():
    prediction = rps_model()
    labels = ['rock','paper','scissors','nothing']
    # max value of the output of the prediction [list] gives us the models prediction of user choice
    us_win_max = labels[np.argmax(prediction)]
    print (f"your choice is: {us_win_max}")
    return us_win_max

# Gets the computer_choice randomly from list of items
def get_computer_choice():
    com_choice = random.choice(items)
    print (f"the computer's choice is: {com_choice}" )
    return com_choice

# Find the winner algorithm
def get_winner(co_choice,us_choice):
    if us_choice == co_choice :
        print("It's a tie!")
    elif us_choice == "rock":
        if co_choice == "scissors":
            print("You win!")

            return 1 
        else:
            print("You lose!")
            return 2 
 
    elif us_choice == "paper":
        if co_choice == "scissors":
            print("You lose!")
            return 1
        else:
            print("You win!")
            return 2 

    elif us_choice == "scissors":
        if co_choice == "rock":
            print("You lose!")
            return 1
        else:
            print("You win!")
            return 2 
            
    if us_choice == 'nothing':
        print("You didn't play this round :(")
    
# main game function
def play():
    computer_wins = 0
    user_wins = 0
    
    while True:
        us_choice_final = get_user_choice()
        com_choice_final = get_computer_choice()
        winner = get_winner(com_choice_final,us_choice_final)
        #winner = 1
        #print (winner)
        if (winner == 2):
            user_wins += 1
            print('User wins the round!!!')
            
        elif (winner == 1):
            computer_wins += 1
            print('Computer wins the round!!!')

        print(f"The computer score is: {computer_wins} and the player score is: {user_wins}")
        if  computer_wins == 3:
        
            print('Computer wins the game! Tis a rematch!')
            computer_wins = 0 
            user_wins = 0   

        elif user_wins == 3:
            print('User wins the game! Tis a rematch!')
            computer_wins = 0 
            user_wins = 0  

        if cv2.waitKey(1) & 0xFF == ord('q'):            
            break
            
        play_again = input("Play again? (y/n): ")
         

        if play_again.lower() == "n":
            exit()

play()