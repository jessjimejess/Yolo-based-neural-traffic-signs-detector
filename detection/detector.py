import cv2
import os
import numpy as np
import time
import threading
import math

# --------------------- Unitary test ----------------- 

NET_FILE = "C:/darknet/build/darknet/x64/custom/yolov3.cfg"
W_FILE = "C:/darknet/build/darknet/x64/backup/yolov3_last.weights"
imgframe = "detection/bb.jpg"
threshold = 0.25

# --------------------- Unitary test -------------------

def netbuild(NET_FILE, W_FILE):
    net = cv2.dnn.readNetFromDarknet(NET_FILE, W_FILE)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
    layers = net.getLayerNames()
    output_layers = [layers[i[0] - 1] for i in net.getUnconnectedOutLayers()]  
    return net, output_layers

def drawboxes(frame,foundectlist):
    height, width = frame.shape[:2]
    for detection in foundectlist:

        centerx = detection["centerx"] * width
        centery = detection["centery"] * height
        sqwidth = detection["sqwidth"] * width
        sqheight = detection["sqheight"] * height
    
        leftupcornerx = centerx - (sqwidth / 2)
        leftupcornery = centery - (sqheight / 2)

        cv2.rectangle(frame, (int(leftupcornerx), int(leftupcornery)), (int(leftupcornerx) + int(sqwidth), int(leftupcornery) + int(sqheight)), (255, 0, 0), 2)

    
    cv2.imshow("polc", frame)
    cv2.waitKey(1) 
    

def detection(net, output_layers, frame, threshold):
  
    dectdict = {}
    foundectlist = []
    
    imgcut = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),swapRB=True, crop=False)
    
    net.setInput(imgcut)
    layer_outputs = net.forward(output_layers)
    
   
    # thread = threading.Thread(target=thread, args=(layer_outputs))
    
    for output in layer_outputs:
        
        for detection in output:
            
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            start = time.time()
            if confidence > threshold:
                print(confidence)
                dectdict = {"centerx":detection[0], "centery":detection[1], "sqwidth":detection[2], "sqheight":detection[3]}
                foundectlist.append(dectdict)
    
    drawboxes(frame,foundectlist)
    
    

# ------------- Unitary test ----------------- #
if __name__ == "__main__":

    net, output_layers = netbuild(NET_FILE, W_FILE)
    
    cap = cv2.VideoCapture("detection/Granada.mp4")
    while True:


        ret, frame = cap.read()
    
        detection(net, output_layers, frame, threshold)
        