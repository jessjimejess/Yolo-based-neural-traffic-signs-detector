import socket
import cv2
import numpy
import struct
import time
from detector import netbuild, detection
import zlib

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
            imgsize = conn.recv(16)

            stringimg = conn.recv(int(imgsize))
            
            
            while len(stringimg) < int(imgsize):
                img = conn.recv(int(imgsize))
                stringimg += img

            dd = zlib.decompressobj().decompress(stringimg)
            
            data = numpy.fromstring(dd, dtype='uint8').reshape(416, 416, 3)  #Change for image size
            
            detection(net, output_layers, data, threshold)
            
            conn.sendall(b'received')
