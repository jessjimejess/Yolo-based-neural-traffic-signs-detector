import socket
import cv2
import numpy

HOST = '192.168.0.150'
PORT = 65432

RPIADDR = '192.168.0.129'
RPIPORT = 65443

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    
    s.bind((HOST,PORT))
    s.connect((RPIADDR, RPIPORT))
    




    while True:
        
        stringimg = b""

        while len(stringimg) < 750000:
            chunk, addr = s.recvfrom(65507)
            stringimg = stringimg + chunk
            #print(len(stringimg))

        data = numpy.fromstring(stringimg, dtype='uint8').reshape(500, 500, 3)
        cv2.imshow("image", data)

        s.sendto(b"ok", (RPIADDR, RPIPORT))
        cv2.waitKey(1)
