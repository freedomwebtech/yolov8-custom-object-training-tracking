import cv2    
import time
cpt = 0
maxFrames = 100 # if you want 5 frames only.


cap=cv2.VideoCapture('surf.mp4')
while cpt < maxFrames:
    ret, frame = cap.read()
    frame=cv2.resize(frame,(1080,500))
    time.sleep(0.01)
    frame=cv2.flip(frame,1)
    cv2.imshow("test window", frame) # show image in window
    cv2.imwrite(r"C:\Users\freed\Downloads\safety\rpi4-yolov8-custom-segmentation-main\rpi4-yolov8-custom-segmentation-main\img\myimages\surfing_%d.jpg" %cpt, frame)
    cpt += 1
    if cv2.waitKey(5)&0xFF==27:
        break
cap.release()   
cv2.destroyAllWindows()
