import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector
import random
import time
from keras.models import load_model
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

detector = HandDetector(maxHands = 1)

timer = 0
game_stat = False
startGame = False
scores = [0,0] #[AI,player]

model = load_model('keras_model.h5', compile= False)
#video
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


while True:
    main_screen = cv2.imread("Resources/BG.png")
    ret, img = cap.read()

    resized_frame = cv2.resize(img,(0,0),None,0.875,0.875)
    resized_frame = resized_frame[:,80:480]
    # Find Hands
    hands, img = detector.findHands(resized_frame) #
    
    if startGame:
        if game_stat is False:
            timer = time.time() - initialTime
            cv2.putText(main_screen,str(int(timer)),(605,435),cv2.FONT_HERSHEY_PLAIN,6,(255,0,255),4)

            if timer > 3:
                game_stat = True
                timer = 0

                if hands:
                    playerMove = None
                    hand = hands[0]
                    image_np = np.array(resized_frame)
                    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image (what that mean?!)
                    data[0] = normalized_image
                    prediction = model.predict(data)
                    # gets uset choice
                    #get this bit from the labels.txt file if u can
                    labels = ['rock','paper','scissors','nothing']
                    user_choice = labels[np.argmax(prediction)]
                    if user_choice == 'rock':
                        playerMove = 1
                    if user_choice == 'paper':
                        playerMove = 2
                    if user_choice == 'scissors':
                        playerMove = 3

                    random_number = random.randint(1,3)
                    com_choice_img = cv2.imread(f'Resources/{random_number}.png', cv2.IMREAD_UNCHANGED)
                    main_screen = cvzone.overlayPNG(main_screen,com_choice_img,(149,310))

                    # Player Wins
                    if (playerMove == 1 and random_number == 3) or \
                            (playerMove == 2 and random_number == 1) or \
                            (playerMove == 3 and random_number == 2):
                        scores[1] += 1
 
                    # AI Wins
                    if (playerMove == 3 and random_number == 1) or \
                            (playerMove == 1 and random_number == 2) or \
                            (playerMove == 2 and random_number == 3):
                        scores[0] += 1
                    print(playerMove)


    main_screen[234:654,795:1195] = resized_frame

    if game_stat:
        main_screen = cvzone.overlayPNG(main_screen,com_choice_img,(149,310))

    cv2.putText(main_screen,str(scores[0]),(410,215),cv2.FONT_HERSHEY_PLAIN,6,(255,0,255),4)
    cv2.putText(main_screen,str(scores[1]),(1112,215),cv2.FONT_HERSHEY_PLAIN,6,(255,0,255),4)


    cv2.imshow("BG",main_screen)

    key = cv2.waitKey(1)
    
    if key == ord('s'):
        startGame = True
        initialTime = time.time()
        game_stat = False
