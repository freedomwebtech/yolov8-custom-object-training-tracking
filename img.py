import cv2
import time
from vidgear.gears import CamGear    
import time
cpt = 0
maxFrames = 100 # if you want 5 frames only.
#stream = CamGear(source='https://www.youtube.com/watch?v=3o9aoRyrvAk', stream_mode = True, logging=True).start() # YouTube Video URL as input

cap=cv2.VideoCapture('surf.mp4')
#start_frame_number = 50
#cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame_number)
while cpt < maxFrames:
    ret, frame = cap.read()
#    frame=stream.read() 
    frame=cv2.resize(frame,(1080,500))
    time.sleep(0.01)
    frame=cv2.flip(frame,1)
    cv2.imshow("test window", frame) # show image in window
    cv2.imwrite(r"C:\Users\freed\Downloads\safety\rpi4-yolov8-custom-segmentation-main\rpi4-yolov8-custom-segmentation-main\img\myimages\surfing_%d.jpg" %cpt, frame)
#    time.sleep(0.01)
    cpt += 1
    if cv2.waitKey(5)&0xFF==27:
        break
cap.release()
#stream.stop()   
cv2.destroyAllWindows()