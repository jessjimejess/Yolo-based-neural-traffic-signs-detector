from picamera.array import PiRGBArray, PiBayerArray, PiYUVArray
import picamera
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
s.connect((HOST, PORT))
print("connected")
time.sleep(3)

camera = picamera.PiCamera()
camera.resolution = (416,416)
stream = PiRGBArray(camera,size=(416,416)) 


while True:
    
    for frame in camera.capture_continuous(stream,'bgr',use_video_port=True):
		
	cd = zlib.compress(stream.array.tostring(), 2)
	imgsize = str(len(cd)).ljust(16)
    	
	s.sendall(imgsize)
   	s.sendall(cd)
	
    	stream.seek(0)
	stream.truncate()
        
    
	
   





