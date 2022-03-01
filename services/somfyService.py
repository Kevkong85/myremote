import RPi.GPIO as GPIO
import time

class somfyService:
    PIN_UP = 26
    PIN_DOWN = 16
    DURATION_IN_S = 25

    def __init__(self):
        print("somfyService: init")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(somfyService.PIN_UP, GPIO.OUT)
        GPIO.setup(somfyService.PIN_DOWN, GPIO.OUT)
        GPIO.output(somfyService.PIN_UP, GPIO.LOW)
        GPIO.output(somfyService.PIN_DOWN, GPIO.LOW)

    def moveDown(self):
        GPIO.output(somfyService.PIN_DOWN, GPIO.HIGH)
        time.sleep(somfyService.DURATION_IN_S)
        GPIO.output(somfyService.PIN_DOWN, GPIO.LOW)

    def moveUp(self):
        GPIO.output(somfyService.PIN_UP, GPIO.HIGH)
        time.sleep(somfyService.DURATION_IN_S)
        GPIO.output(somfyService.PIN_UP, GPIO.LOW)
