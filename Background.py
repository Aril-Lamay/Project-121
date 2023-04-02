import cv2
import time
import numpy as np

image = cv2.imread("OIP.jpeg")
capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    frame = cv2.resize(frame, (640, 480)) 
    image = cv2.resize(image, (640, 480)) 
    u_black = np.array([104, 153, 70]) 
    l_black = np.array([30, 30, 0]) 
  
    mask = cv2.inRange(frame, l_black, u_black) 
    res = cv2.bitwise_and(frame, frame, mask = mask) 
  
    f = frame - res 
    f = np.where(f == 0, image, f) 
  
    cv2.imshow("capture", frame) 
    cv2.imshow("mask", f) 
  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
  
capture.release() 
cv2.destroyAllWindows() 