import cv2,time
video=cv2.VideoCapture('http://192.168.43.181:8080/video')
a=0

while True:
    
    a+=1
    check, frame=video.read()
    
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print(check)
    print(frame)
    #time.sleep(2)
    
    cv2.imshow("Capturing",gray)
    key=cv2.waitKey(1)
    
    if key==ord('q'):
        break
    
print(a)    
video.release()
cv2.destroyAllWindows() 

