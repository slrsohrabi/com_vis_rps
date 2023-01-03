import cv2
from keras.models import load_model
import numpy as np
import random
import time

items = ["rock", "paper", "scissors"]
model = load_model('keras_model.h5', compile= False)
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
computer_wins = 0
user_wins = 0

def play_game():

    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        print("Rock, Paper, Scissors?")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        us_choice_final = get_user_choice(prediction)
        com_choice_final = get_computer_choice()
        #print(f"The computer score is: {computer_wins} and the player score is: {user_wins}")
        time.sleep(3)
        get_winner(com_choice_final,us_choice_final)
      

        if cv2.waitKey(1) & 0xFF == ord('q'):            
            break
        play_again = input("Play again? (y/n): ")
        if play_again.lower() == "n":
            break

def get_user_choice(p1):
    labels = ['rock','paper','scissors','nothing']
    us_win_max = labels[np.argmax(p1)]
    print (f"your choice is: {us_win_max}")
    return us_win_max

def get_computer_choice():
    com_choice = random.choice(items)
    print (f"the computer's choice is: {com_choice}" )
    return com_choice


def get_winner(co_choice,us_choice):

    
    if us_choice == 'nothing':
        print("You didn't play this round :(")
    if us_choice == co_choice :
        print("It's a tie!")
    elif us_choice == "rock":
        if co_choice == "scissors":
            print("You win!")
            user_wins += 1 
        else:
            print("You lose!")
            computer_wins += 1 
    elif us_choice == "paper":
        if co_choice == "scissors":
            print("You lose!")
            computer_wins += 1
        else:
            print("You win!")
            user_wins += 1 

    elif us_choice == "scissors":
        if co_choice == "rock":
            print("You lose!")
            computer_wins += 1
        else:
            print("You win!")
            user_wins += 1 
    print(f"The computer score is: {computer_wins} and the player score is: {user_wins}")
    if (user_wins == 3):
        print('Game Over! User wins the game!!!')
        
    elif (computer_wins == 3):
        print('Game Over! Computer wins the game!!!')
        

play_game()

    
        
    


