import RPi.GPIO as GPIO
import sys
import time

class Button():
    def __init__(self, pin, call_back):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN, pull_up_down= GPIO.PUD_UP)
        GPIO.add_event_detect(self.pin, GPIO.RISING, callback= call_back, bouncetime= 300)

    def __del__(self):
        GPIO.remove_event_detect(self.pin)

if __name__ == '__main__':
    print('- Button -')
    GPIO.setmode(GPIO.BCM)
    pin = int(sys.argv[1])
    def f(channel):
        print('push')
    button = Button(pin, f)
    while True:
        print('wait ...')
        time.sleep(0.5)
