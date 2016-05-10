import time
import picamera
import io
import base64
import cv2
import numpy as np
import os
from PIL import Image
from socketIO_client import SocketIO ,BaseNamespace
HOST = 'http://pibot.herokuapp.com'
PORT = 80
nodeSocket = SocketIO(HOST, PORT)

my_file = open('my_image.jpg', 'wb')
with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    camera.capture(my_file)
my_file.close()
img = Image.open('my_image.jpg').convert("RGB")
img.save('toserver.webp',"WEBP")
with open('toserver.webp','rb') as image_file:
    send = base64.b64encode(image_file.read())
    print send
    nodeSocket.emit('stream', 'data:image/webp;base64,'+send)
image_file.close()
camera.close()
    
