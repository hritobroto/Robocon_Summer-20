import cv2
import numpy as np

video=cv2.VideoCapture(1)
#for using the webcam, use cv2.VideoCapture(0)

def canny(frame,sigma=0.33):
    med=np.median(frame);
    low=int(max(0,(1.0-sigma)*med));
    up=int(min(255,(1.0+sigma)*med));
    edge=cv2.Canny(frame,low,up);
    return edge;

while(True):
    _, frame=video.read();
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV);
    low=np.array([0,0,0]);
    high=np.array([0,255,255]);
    mask=cv2.inRange(hsv,low,high);
    #gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #black=cv2.bitwise_and(frame,frame,mask=mask);
    blurred=cv2.GaussianBlur(mask,(3,3),0)
    disp=canny(blurred);
    
    cv2.imshow("frame",disp);

    key=cv2.waitKey(1);
    if(key==27):
        cv2.destroyAllWindows();
        break;
