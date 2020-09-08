
from picamera.array import PiRGBArray, PiBayerArray, PiYUVArray
import picamera
import select
import socket
import time
import cv2
import numpy
import io
import struct
import zlib
import binascii
import time
HOST = '192.168.1.102'  # The server's hostname or IP address
PORT = 65432        # The port used by the server




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
s.connect((HOST, PORT))
print("connected")
time.sleep(3)


camera = picamera.PiCamera()
camera.resolution = (416,416)
#stream = picamera.array.PiYUVArray(camera) 
stream = io.BytesIO()


    
for frame in camera.capture_continuous(stream,'jpeg', use_video_port=True):
   	
    #cd = zlib.compress(stream.array.tostring(), 2)
    stream.seek(0)
    cd = zlib.compress(stream.read())
    imgsize = str(len(cd)).ljust(16)
	    	
    s.sendall(imgsize)
    s.sendall(cd)
	
    stream.seek(0)
    stream.truncate()
	
    readable, writable, exceptional = select.select([s], [], [], 0.001)
	
    if readable:         
        data = s.recv(8)
	print(data)
    	img = s.recv(int(data))
	print(str(img))
   





