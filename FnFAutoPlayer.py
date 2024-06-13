import numpy as np
from PIL import ImageGrab 
import cv2
import time
import pyautogui as km
import keyboard
import mss
import threading



def startUp():
    cv2.namedWindow("dst", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("dst", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    a,b,screenWidth,screenHeight = cv2.getWindowImageRect('dst')
    cv2.destroyWindow("dst")
    return a,b,screenWidth,screenHeight

x, y, screenHeight, screenWidth = startUp()
print(x)
print(y)
print(screenHeight)
print(screenWidth)

left = 1395
upper = 160
right = 2180
lower = 180
ScreenGrabCoords = left, upper, right, lower  

default_color = (173, 163, 135)
pixHeight = 10
leftPix = 56 
rightPix = 770  
upPix = 540  
downPix = 315 


def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask,vertices,266)
    masked = cv2.bitwise_and(img, mask)
    return masked
def process_img(ogimg):
    processed_img = np.array(ogimg)
    processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGRA2BGR)
    # processed_img =cv2.circle(processed_img, (leftPix,pixHeight), radius=0, color=(0,255,0),thickness=-1)
    return processed_img

def hold_key(key, hold_time):
    start = time.time()
    while time.time() - start < hold_time:
        km.keyDown(key)
    km.keyUp(key)

def hold_Up(hold_time):
    threading.Thread(target=hold_key, args=('up', hold_time)).start()

def hold_Down(hold_time):
    threading.Thread(target=hold_key, args=('down', hold_time)).start()

def hold_Left(hold_time):
    threading.Thread(target=hold_key, args=('left', hold_time)).start()

def hold_Right(hold_time):
    threading.Thread(target=hold_key, args=('right', hold_time)).start()
    

def main():
    
    print("Press 'o' to start...")
    while not keyboard.is_pressed('o'):
        time.sleep(0.1)  # Polling interval

    print("Starting control...")
    last_time = time.time()
    with mss.mss() as sct:
        while True:
            screen = sct.grab(ScreenGrabCoords)
            new_screen = process_img(screen)
            height = screen.height
            width = screen.width

        
            #controll code         
            if (new_screen[5,54] != default_color).any():
                #print(new_screen[10,20])
                print("left")
                # colorCheck
                # print(new_screen[5,3])
                hold_Left(0.1)
            if (new_screen[pixHeight,296]!= default_color).any():
                #print(new_screen[10,362])
                print("down")
                # colorCheck
                # print(new_screen[10,296])
                hold_Down(0.1)
            if (new_screen[pixHeight,500]!= default_color).any():
                #print(new_screen[10,454])
                print("go up")
                # colorCheck
                # print(new_screen[10,525])
                hold_Up(0.1)
            if (new_screen[10,765]!= default_color).any():
                #print (new_screen[10,700])
                print("go right")
                # colorCheck
                # print(new_screen[10,770])
                hold_Right(0.1)
                
            # #insta lose 💀
            # if keyboard.is_pressed("o"):
            #     hold_Right(0.1)
            #     time.sleep(0.1)
            # ok so pyautogui works with fnf
            # else:
                # print("clear!")
            # time.sleep(0.001)
            """was to debug angle (still is a bitch btw)
            if keyboard.is_pressed('o'):
                mouseLeft90()
                dubug += 1
                print(dubug)"""

            font = cv2.FONT_HERSHEY_SIMPLEX
            elapsed_time = time.time() - last_time
            # fps = 1 / elapsed_time


            # cv2.putText(new_screen, f"Elapsed Time: {elapsed_time:.2f} seconds", (10, 20), font, 1, (0, 255, 0), 2)
            
            cv2.imshow('FNFAUTOPLAYER🫦', new_screen)
            
            #//(old screenshowcode) cv2.imshow('window',cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2RGB))
            if cv2.waitKey(25) & 0xff == ord('q'):
                cv2.destroyAllWindows()
                break
            # print("FPS: {:.2f}".format(fps))
            last_time = time.time()
#execute here \/
main()