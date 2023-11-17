from PIL import Image
from tkinter import *
import time
import pytesseract
from threading import Thread
import cv2
import serial
ser = serial.Serial('/dev/ttyACM0')
ser.baudrate = 9000
cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)
while(vc.isOpened()):
    finished = False
    ret,frame=vc.read()
    def reader():
        text = pytesseract.image_to_string(frame)
        file = open('read.txt', 'w') 
        file.write(text)
        print(text)
        file.close()
        ser.write(bytes(text,'utf-8'))
        time.sleep(3)
    scan = Thread(target=reader)
    scan.start()
    cv2.imshow('Video',frame)
    time.sleep(0.1)
    if cv2.waitKey(1) & 0xFF ==ord('e'):
        break
    time.sleep(0.15)
    scan.join


vc.release()
cv2.destroyWindow("preview")

    