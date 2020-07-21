import cv2
import numpy as np
cap=cv2.VideoCapture(0)
#back=cv2.imread('./image.jpg')
while cap.isOpened():
    ret,back=cap.read()
    if ret:  #check for camera working
        cv2.imshow('image',back) #back is what camera is reading
        if cv2.waitKey(5)==ord('q'):
            cv2.imwrite('image.jpg',back)
            break
cap.release()
cv2.destroyAllWindows()