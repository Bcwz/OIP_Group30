# https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/7
from picamera import PiCamera
from time import sleep

camera = PiCamera()

def video():     
    camera.resolution = (1920,1080)
    camera.framerate = 60
    camera.start_preview(alpha=200)
    sleep(5)
    camera.stop_preview()
    
def image():
    camera.resolution = (2592,1944)
    camera.framerate = 15
    camera.start_preview()
    camera.capture('/home/pi/Desktop/max.jpg')
    camera.stop_preview()
    
#video()
#image()
