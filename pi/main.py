# main py loop
import time
import picamera
import socket
import io
#https://gist.github.com/marvin/4318413
HOST = 'https://pibot.herokuapp.com/livefeed'
PORT = 80
ADDR = (HOST,PORT)
#BUFSIZE = 4096
#videofile = "videos/royalty-free_footage_wien_18_640x360.mp4"

#bytes = open(videofile).read()

#print len(bytes)

#client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client = socket.socket()
client.connect(ADDR)
connection = client.makefile('wb')
try:
    with picamera.PiCemara() as camera:
        camera.resolution = (640, 480)
        camera.framerate = 24
        # Start a preview and let the camera warm up for 2 seconds
        camera.start_preview()
        time.sleep(2)
        # Start recording, sending the output to the connection for 60
        # seconds, then stop
        camera.start_recording(connection, format='h264')
finally:
    connection.close()
    client.close()
#client.send(bytes)

#client.close()
