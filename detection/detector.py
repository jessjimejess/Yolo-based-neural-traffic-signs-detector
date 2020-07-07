import cv2
import os
import numpy as np
NET_FILE = "C:/darknet/build/darknet/x64/custom/yolov3.cfg"
W_FILE = "C:/darknet/build/darknet/x64/backup/yolov3_last.weights"


def netbuild():
    net = cv2.dnn.readNetFromDarknet(NET_FILE, W_FILE)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

    return net

def detection():
    net = netbuild()
    frame = cv2.imread("detection/3.jpg")
    imgcut = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),swapRB=True, crop=False)
    layers = net.getLayerNames()
    output_layers = [layers[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    net.setInput(imgcut)
    layer_outputs = net.forward(output_layers)

    for output in layer_outputs:
        
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if(confidence > 0):
                print(confidence, class_id)



if __name__ == "__main__":
    detection()