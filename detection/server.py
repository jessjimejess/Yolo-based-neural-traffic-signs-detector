import socket
import cv2
import numpy
import struct

HOST = '192.168.1.102'
PORT = 65432
imgbuffer = 640*480*3

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((HOST,PORT))
    s.listen()

    print("waiting for a connection")
    conn, addr = s.accept()

    with conn:
        print("conected by", addr)
        
        while True:

            #print("waiting for data")
            #imgsize = conn.recv(16)
            #print(int(imgsize))
           
            stringimg = conn.recv(int(640*480*3))
        
        
            while len(stringimg) < int(640*480*3):
                img = conn.recv(int(640*480*3))
                stringimg += img
                                 
            data = numpy.fromstring(stringimg, dtype='uint8').reshape(480, 640, 3)  #Change for image size
            #data = struct.unpack
            cv2.imshow('hola', data)
            cv2.waitKey(1)
            
            conn.sendall(b'received')
