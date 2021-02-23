from picamera import PiCamera
from time import sleep
from gpiozero import Button
from datetime import datetime

camera = PiCamera()

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
button = Button(4)

global var
var = 0
#takes 10 pictures then quits
while var < 10 : 
    button.wait_for_press()

    def takePic():
        camera.start_preview()
        camera.annotate_text = dt_string
        sleep(4)
        num = var
        naming = num + ".jpg"
        camera.capture('/home/pi/Desktop/image', naming)
        camera.stop_preview()
        var = var + 1

    takePic()

