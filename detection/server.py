import socket
import cv2
import numpy
import struct
import time
import zlib
import threading
import time
from detector import netbuild, detection


compressed_image = b''
dataR = b''

# -- Thread function
def detectWorker(net,output_layers,threshold,HOST,PORT,imgbuffer, conn, colourlist):
    global compressed_image
    global dataR
    
    print("Thread: ", threading.currentThread().getName(), "starting - Initializing conv net")
    time.sleep(5)
    oldframe = b''

    if compressed_image != b'':

        while 1:
            
            starttime = time.time()

            while oldframe == compressed_image:
                next
            
            stringimg = compressed_image
            oldframe = compressed_image
            dd = zlib.decompressobj().decompress(stringimg)
            image = cv2.imdecode(numpy.fromstring(dd, numpy.uint8), cv2.IMREAD_COLOR)
            # cv2.waitKey(1000)
            # dd = cv2.cvtColor(image,cv2.COLOR_YUV2BGR_I420)
            # data = numpy.fromstring(dd, dtype='uint8').reshape(416, 416, 3)  #Change for image size
            dataR = detection(net, output_layers, image, threshold, colourlist, starttime)



def receiveAndDetect(conn):
    global compressed_image
    global dataR
    
    while True:
        
        imgsize = conn.recv(16)
        stringimg = conn.recv(1024)
        

        while len(stringimg) < int(imgsize):
            img = conn.recv(int(imgsize) - len(stringimg))
            stringimg += img

        compressed_image = stringimg

        if dataR != b'':
            size = str(len(dataR)).ljust(8).encode()
            conn.sendall(size)
            conn.sendall(dataR.encode())







if __name__ == "__main__":

    # ---------------- Yolo configuration ---------------------- #
    NET_FILE = "C:/darknet/build/darknet/x64/custom/yolov3.cfg"
    W_FILE = "C:/darknet/build/darknet/x64/backup/yolov3_6000.weights"
    O_FILE = "C:/darknet/build/darknet/x64/data/obj.names"
    threshold = 0.25

    # -------------- Socket configuration --------------------- #
    HOST = '192.168.1.102'
    PORT = 65432
    imgbuffer = 416*416*3
    net, output_layers, colourlist = netbuild(NET_FILE, W_FILE,O_FILE)
    print(colourlist)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.bind((HOST,PORT))
        s.listen()
        print("waiting for a connection")
        conn, dird = s.accept()


        with conn:
            print("conected")
            print("Main: initializing threads -")
            t = threading.Thread(name='thr1', target=detectWorker, args=(net,output_layers,threshold,HOST,PORT,imgbuffer, conn, colourlist))
            t.start()
            receiveAndDetect(conn)
