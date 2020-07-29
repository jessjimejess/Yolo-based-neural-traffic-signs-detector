import socket
import cv2
import numpy
import struct
import time
import zlib
import threading
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

compressed_image = b""

# -- Thread function
def detectWorker(NET_FILE,W_FILE,threshold,HOST,PORT,imgbuffer):
    global compressed_image
    print("Thread: ", threading.currentThread().getName(), "starting - Initializing conv net")
    net, output_layers = netbuild(NET_FILE, W_FILE)
    time.sleep(5)
    while 1:

            stringimg = compressed_image
            dd = zlib.decompressobj().decompress(stringimg)
            data = numpy.fromstring(dd, dtype='uint8').reshape(416, 416, 3)  #Change for image size
            detection(net, output_layers, data, threshold)






def receiveAndDetect():

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
                
                global compressed_image
                compressed_image = stringimg

                conn.sendall(b'received')




if __name__ == "__main__":
    
    print("Main: initializing threads -")
    t = threading.Thread(name='thr1', target=detectWorker, args=(NET_FILE,W_FILE,threshold,HOST,PORT,imgbuffer))
    t.start()
    receiveAndDetect()
