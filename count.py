import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
from tracker import *
from vidgear.gears import CamGear    
import time
model=YOLO('best.pt')


list1=[]
def order(lst):
    ascending = descending = True
    for i in range(len(lst) - 1): 
        if lst[i] > lst[i+1] :
            ascending = False
        elif lst[i] < lst[i+1] :
            descending = False
    return ascending or descending

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        colorsBGR = [x, y]
        print(colorsBGR)
        

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

cap=cv2.VideoCapture('surf.mp4')
#stream = CamGear(source='https://www.youtube.com/watch?v=3o9aoRyrvAk', stream_mode = True, logging=True).start() # YouTube Video URL as input
#cy1=178

my_file = open("coco1.txt", "r")
data = my_file.read()
class_list = data.split("\n") 
k=['car','motorcycle']
#print(class_list)
count=0
tracker=Tracker()   
cy1=179
offset=6
counter=0
area=[(403,289),(390,360),(254,425),(204,353)]
area1=[(2,330),(1,425),(1019,410),(1016,317)]
count1=0
while True:    
    ret,frame = cap.read()
    if not ret:
        break
    
    

#    frame=stream.read()
    count += 1
    if count % 3 != 0:
        continue
    frame=cv2.resize(frame,(1020,500))
    frame=cv2.flip(frame,1)
    results=model.predict(frame)
 #   print(results)
    a=results[0].boxes.boxes
    px=pd.DataFrame(a).astype("float")
#    print(px)
    list=[]
      
    for index,row in px.iterrows():
#        print(row)
 
        x1=int(row[0])
        y1=int(row[1])
        x2=int(row[2])
        y2=int(row[3])
        d=int(row[5])
        c=class_list[d]
        list.append([x1,y1,x2,y2])
    bbox_id=tracker.update(list)
    for bbox in bbox_id:
        x3,y3,x4,y4,id=bbox
        cx=int(x3+x4)//2
        cy=int(y3+y4)//2
#        results=cv2.pointPolygonTest(np.array(area,np.int32),((cx,cy)),False)
#        if results>=0:
        cv2.rectangle(frame,(x3,y3),(x4,y4),(0,255,0),2)
#            cv2.circle(frame,(cx,cy),4,(255,0,255),-1)  
        cv2.putText(frame,str(id),(x4,y4),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
        cv2.putText(frame,str(c),(x3,y3),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),1)

     
#            results1=cv2.pointPolygonTest(np.array(area1,np.int32),((cx,cy)),False)
#            if results1>=0:
#               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
#               cv2.circle(frame,(cx,cy),4,(255,0,255),-1)  
                   
#               l1=(cy//70)  
#        if results>=0:
       
    
        
        
#        results1=cv2.pointPolygonTest(np.array(area1,np.int32),((x4,y4)),False)
#        if results1>=0:
#           cv2.rectangle(frame,(x3,y3),(x4,y4),(0,255,0),2)
#           cv2.circle(frame,(x4,y4),4,(255,0,255),-1)
#           cv2.putText(frame,str(id),(x4,y4),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
#           print(cx//70)
           
    
 
#        cv2.putText(frame,str(c),(x4,y4),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
#           area1.add(id)  
  
 #   l=len(area1)
 #   cv2.putText(frame,str(l),(60,90),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),2)
 #   funct(list1)
 #   cv2.polylines(frame,[np.array(area,np.int32)],True,(0,255,0),2)
#    cv2.polylines(frame,[np.array(area1,np.int32)],True,(0,255,0),2)
#    print('l')
#    print(l)
#    print('l1')
#    print(l1)
    
    print(count1)
    cv2.imshow("RGB", frame)
    if cv2.waitKey(1)&0xFF==27:
        break
#
cap.release()
cv2.destroyAllWindows()
#stream.stop()