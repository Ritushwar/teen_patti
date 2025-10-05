from ultralytics import YOLO
import cv2
import cvzone
import math
import csv
import torch
import numpy as np
import teen_patti
model = YOLO("/home/ritu/teen_patti/my_model.pt")
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
results_dict = {6:"Trail",5:"Doubly",
                    4:"Run",3:"Color",
                    2:"Juut",1:"High Card"}
total_classes = []
classes = model.names
for clss in classes:
    total_classes.append(classes[clss])
frame_number = 0
while True:
    success, img = cap.read()
    if not success:
        break
    pokers = []
    if frame_number % 4 == 0:
        results = model(img)
        for r in results:
            boxes = r.boxes
            for box in boxes:
            # bounding box
                x1,y1,x2,y2 = box.xyxy[0]
                x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
                conf = math.ceil((box.conf[0]*100)) / 100
                clss = int(box.cls[0])
                if conf > 0.4:
                    current_class = total_classes[clss]
                    if current_class not in pokers:
                        pokers.append(current_class)
                    w,h = x2-x1, y2-y1
                    cvzone.cornerRect(img, (x1,y1,w,h),colorC=(0,0,255),l=5)
                    cvzone.putTextRect(img, f'{current_class}',(max(0,x1),max(0,y1)), scale=0.6, thickness=1)
        if len(pokers)==3:
            possibleRanks = int(teen_patti.findPokerHand(pokers)[0])
            pokers=[]
            cvzone.putTextRect(img, f'{results_dict[possibleRanks]}',(max(0,x1-20),max(0,y1-20)), scale=2, thickness=1)
        cv2.imshow("Result",img)
    #img = cv2.resize(img,(frame_width,frame_height))
    #out.write(img)
    frame_number+=1
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    if key == 27:
        break
cap.release()
# out.release()
cv2.destroyAllWindows()

