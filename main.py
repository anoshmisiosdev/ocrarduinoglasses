from PIL import Image
from tkinter import *
import time
import pytesseract
from threading import Thread
import cv2
import serial
import numpy as np

#ser = serial.Serial('/dev/ttyACM0')
#ser.baudrate = 9000
def videomom(frame):
    vc = cv2.VideoCapture(0)
    ret, frame = vc.read()
    cv2.imshow('Video', frame)

def reader(frame):
    cv2.imwrite('make.jpg', frame)
    img = cv2.cvtColor(Image.open('make.jpg'), cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(img)
    print(text)
    #ser.write(bytes(text,'utf-8'))
    time.sleep(3)
cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)
while(vc.isOpened()):
    video = Thread()
vc.release()
cv2.destroyWindow("preview")




















