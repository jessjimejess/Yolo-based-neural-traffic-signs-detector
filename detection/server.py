import socket
import cv2
import numpy
import struct
import time
from detector import netbuild, detection

# ---------------- Yolo configuration ---------------------- #
NET_FILE = "C:/darknet/build/darknet/x64/custom/yolov3.cfg"
W_FILE = "C:/darknet/build/darknet/x64/backup/yolov3_last.weights"
threshold = 0.25

# -------------- Socket configuration --------------------- #
HOST = '192.168.1.102'
PORT = 65432
imgbuffer = 416*416*3

net, output_layers = netbuild(NET_FILE, W_FILE)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((HOST,PORT))
    s.listen()

    print("waiting for a connection")
    conn, dird = s.accept()

    with conn:
        print("conected")
        
        while True:

            stringimg = conn.recv(int(416*416*3))
            
            while len(stringimg) < int(416*416*3):
                img = conn.recv(int(416*416*3))
                stringimg += img

            
            data = numpy.fromstring(stringimg, dtype='uint8').reshape(416, 416, 3)  #Change for image size
            
            start = time.time()
            detection(net, output_layers, data, threshold)
            finish = time.time()
            print(str(finish-start))
            
            conn.sendall(b'received')
