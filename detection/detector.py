import cv2
import os
import numpy as np
import time
import threading
import math



def netbuild(NET_FILE, W_FILE, O_FILE):
    net = cv2.dnn.readNetFromDarknet(NET_FILE, W_FILE)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
    layers = net.getLayerNames()
    output_layers = [layers[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    f = open(O_FILE)
    linenumber = f.readlines()
    colourlist = [list(np.random.choice(range(256), size=3)) for i in range(len(linenumber))]

    return net, output_layers, colourlist

def drawboxes(frame,foundectlist, colourlist, starttime):
    height, width = frame.shape[:2]
    
    for detection in foundectlist:
        centerx = detection["centerx"] * width
        centery = detection["centery"] * height
        sqwidth = detection["sqwidth"] * width
        sqheight = detection["sqheight"] * height
    
        leftupcornerx = centerx - (sqwidth / 2)
        leftupcornery = centery - (sqheight / 2)
        colour = colourlist[int(detection["classid"])]
        cv2.rectangle(frame, (int(leftupcornerx), int(leftupcornery)), (int(leftupcornerx) + int(sqwidth), int(leftupcornery) + int(sqheight)), (int(colour[0]), int(colour[1]), int(colour[2])), 2)
        
    fps = int(1 / (time.time() - starttime)) + 1
    image = cv2.putText(frame, "FPS:" + str(fps), (50, 50) , cv2.FONT_HERSHEY_SIMPLEX ,  1, (255, 0, 0) , 2, cv2.LINE_AA) 
    cv2.imshow("polc", frame)
    cv2.waitKey(1)
    

def detection(net, output_layers, frame, threshold, colourlist, starttime):
    
    dectdict = {}
    foundectlist = []
    imgcut = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),swapRB=True, crop=False)
    net.setInput(imgcut)
    layer_outputs = net.forward(output_layers)
    
    for output in layer_outputs:
        
        for detection in output:
            
            scores = detection[5:12]
            class_id = np.argmax(scores)
            confidence = float(scores[class_id])
            
            if confidence > 0.25:
                dectdict = {"classid": class_id, "centerx":detection[0], "centery":detection[1], "sqwidth":detection[2], "sqheight":detection[3]}
                foundectlist.append(dectdict)
    
    drawboxes(frame,foundectlist, colourlist , starttime)
    if len(foundectlist) != 0:
        return str(foundectlist)
    else:
        return b''
        


# ---- Testing ---- #
if __name__ == "__main__":
    

    NET_FILE = "C:/darknet/build/darknet/x64/custom/yolov3.cfg"
    W_FILE = "C:/darknet/build/darknet/x64/backup/yolov3_last.weights"
    frame = "detection/bb.jpg"
    threshold = 0.25

    net, output_layers, colourlist = netbuild(NET_FILE, W_FILE)
    
    cap = cv2.VideoCapture("detection/Granada.mp4")
    while True:


        ret, frame = cap.read()
    
        detection(net, output_layers, frame, threshold)
        