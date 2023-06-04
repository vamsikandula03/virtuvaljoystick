import cv2
import keyboard
import mediapipe as mp
import pyautogui as pyt
import keyboard as kk
#(400,180),(400,280),(300,180),(300,280)
mphands=mp.solutions.hands
hands=mphands.Hands()
mpdraw=mp.solutions.drawing_utils
def fingerup(pos):
    flags=[0,0]

    if pos[8][1]<pos[7][1]:
        flags[0]=1
    else:
        flags[0]=0
    if pos[12][1]<pos[11][1]:
        flags[1]=1
    else:
        flags[1]=0

    return flags
cap=cv2.VideoCapture(0)
while cap.isOpened():
  success,img=cap.read()
  img = cv2.flip(img, 1)
  imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  results = hands.process(imgRGB)
  if results.multi_hand_landmarks:
      for handlms in results.multi_hand_landmarks:
          positions = {}
          for id, lm in enumerate(handlms.landmark):
              h, w, c = img.shape

              cx, cy = int(lm.x * w), int(lm.y * h)
              positions[id]=[cx,cy]

              if id==8:
                  # print(cx,cy)
                  img = cv2.circle(img, (cx, cy), 2, (255, 255, 0), 10)
                  if(cx<400 and cx>300 and cy<280 and cy>180):
                     # print("idle")
                     kk.release('w')
                     kk.release('s')
                     kk.release('d')
                     kk.release('a')
                     # if(fingerup(positions)==[1,1]):
                     #     keyboard.press('space')
                     #     keyboard.release('space')


                  if(cx>400):
                      # pyt.press('D',presses=20)
                      kk.press('d')
                      kk.release('a')
                      # print("D")
                  if(cx<300):
                    kk.press('a')
                    kk.release('d')

                      # print("A")
                  if(cy>280):
                      kk.press('s')
                      kk.release('w')
                      # pyt.press('S',presses=20)
                      # print("S")

                  if(cy<180):
                      # print("W")
                      kk.press('w')
                      kk.release('s')
                      # pyt.press('W',presses=20)
          # print(positions)




  img=cv2.circle(img,(400,180),3,(255,0,0),10)
  img = cv2.circle(img, (400, 280), 3, (255, 0, 0), 10)
  img = cv2.circle(img, (300, 180), 3, (255, 0, 0), 10)
  img = cv2.circle(img, (300, 280), 3, (255, 0, 0), 10)

  cv2.imshow("innn",img)

  cv2.waitKey(1)