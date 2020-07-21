import cv2
import numpy as np
cap=cv2.VideoCapture(0)
back=cv2.imread('./image.jpg')
while cap.isOpened():
    ret,frame=cap.read()
    if ret: #to convert from rgb to hsv
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        #cv2.imshow('hsv',hsv)
        red=np.uint8([[[0,0,255]]])
        hsv_red=cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
        #print(hsv_red)
        l_red=np.array([0,100,100])
        u_red=np.array([10,255,255])
        
        #only red is showing white
        mask=cv2.inRange(hsv,l_red,u_red)
        #cv2.imshow('mask',mask)
        
        #part1 red is showing back image 
        part1=cv2.bitwise_and(back,back,mask=mask)
        #cv2.imshow('part1',part1)
        
        mask=cv2.bitwise_not(mask)
        
        #part2 red is showing colour
        part2=cv2.bitwise_and(frame,frame,mask=mask)
        #cv2.imshow('part2',part2)
        
        part3=part1+part2
        kernel=np.ones((1,1),np.uint8)
        final=cv2.morphologyEx(part3,cv2.MORPH_OPEN,kernel)
        
        cv2.imshow('cloak',final)
        
        if cv2.waitKey(5)==ord('q'):
            #cv2.imwrite('image.jpg',frame)
            break
cap.release()
cv2.destroyAllWindows()