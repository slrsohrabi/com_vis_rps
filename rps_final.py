import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector
import random
import time

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

detector = HandDetector(maxHands = 1)

timer = 0
game_status = False
start_game = False
scores = [0,0] #[AI,player]
wnr_score = 1


while True:
    main_screen = cv2.imread("pics/BG.png")
    ret, img = cap.read()
    # resize the captured recording
    resized_image = cv2.resize(img,(0,0),None,0.875,0.875)
    # crop the resized recording from both sides to fit 
    resized_image = resized_image[:,80:480]

    # Find Hands
    hand_found, img = detector.findHands(resized_image) #

    if start_game:

        if game_status is False:
            timer = time.time() - initial_time
            cv2.putText(main_screen,str(int(timer)),(605,435),cv2.FONT_HERSHEY_PLAIN,6,(255,0,255),4)

            if timer > 3:
                game_status = True
                timer = 0

                if hand_found:
                    player_move = None
                    hand = hand_found[0]
                    player_choice = detector.fingersUp(hand)
                    print(player_choice)
                    if player_choice == [0, 0, 0, 0, 0]:
                        player_move = 1
                    if player_choice == [1, 1, 1, 1, 1]:
                        player_move = 2
                    if player_choice == [0, 1, 1, 0, 0]:
                        player_move = 3

                    randomNumber = random.randint(1,3)
                    com_choice_img = cv2.imread(f'pics/{randomNumber}.png', cv2.IMREAD_UNCHANGED)
                    main_screen = cvzone.overlayPNG(main_screen,com_choice_img,(149,310))

                    # Player Wins
                    if (player_move == 1 and randomNumber == 3) or \
                            (player_move == 2 and randomNumber == 1) or \
                            (player_move == 3 and randomNumber == 2):
                        scores[1] += 1
 
                    # AI Wins
                    if (player_move == 3 and randomNumber == 1) or \
                            (player_move == 1 and randomNumber == 2) or \
                            (player_move == 2 and randomNumber == 3):
                        scores[0] += 1
                        
                    if (scores[0] >= wnr_score):
                        main_screen = cvzone.overlayPNG(main_screen,cv2.imread("pics/BG_0.png"))
                        t1 = cv2.waitKey(0)
                        if t1:
                            cap.release()
                            cv2.destroyAllWindows()

                    if (scores[1] >= wnr_score):
                        main_screen = cvzone.overlayPNG(main_screen,cv2.imread("pics/BG_0.png"))
                        t1 = cv2.waitKey(0)
                        if t1:
                            cap.release()
                            cv2.destroyAllWindows()


                    print(player_move)
                    



    main_screen[234:654,795:1195] = resized_image

    if game_status:
        main_screen = cvzone.overlayPNG(main_screen,com_choice_img,(149,310))

    cv2.putText(main_screen,str(scores[0]),(410,215),cv2.FONT_HERSHEY_PLAIN,6,(255,0,255),4)
    cv2.putText(main_screen,str(scores[1]),(1112,215),cv2.FONT_HERSHEY_PLAIN,6,(255,0,255),4)

    cv2.imshow("Salar's rock paper scissors",main_screen)


    key = cv2.waitKey(1)

    if key == ord('s'):
        start_game = True
        initial_time = time.time()
        game_status = False



