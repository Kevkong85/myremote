import time
from rpi_ws281x import PixelStrip, Color

class ledService:

    # Number of LED pixels
    LED_COUNT = 4
    # GPIO pin connected to the pixels (18 uses PWM!)
    LED_PIN = 18
    # LED signal frequency in hertz (usually 800khz)     
    LED_FREQ_HZ = 800000
    # DMA channel to use for generating signal (try 10)
    LED_DMA = 10
    # True to invert the signal (when using NPN transistor level shift)
    LED_INVERT = False
    # Set to 0 for darkest and 255 for brightest
    LED_BRIGHTNESS = 255
    # set to '1' for GPIOs 13, 19, 41, 45 or 53
    LED_CHANNEL = 0

    def __init__(self):
        self.strip = PixelStrip(
            ledService.LED_COUNT,
            ledService.LED_PIN,
            ledService.LED_FREQ_HZ,
            ledService.LED_DMA,
            ledService.LED_INVERT,
            ledService.LED_BRIGHTNESS,
            ledService.LED_CHANNEL
        )
        self.strip.begin()

    def clear(self):
        self.__colorStatic(Color(0, 0, 0))

    def staticGreen(self):
        self.__colorStatic(Color(0, 255, 0))

    def staticOrange(self):
        self.__colorStatic(Color(255, 103, 0))

    def flashOrange(self):
        self.__colorFlash(Color(255, 103, 0))

    def flashGreen(self):
        self.__colorFlash(Color(0, 255, 0))

    def circleRed(self):
        self.__circle(Color(127, 0, 0))

    def __circle(self, color, wait_ms=50, iterations=10):
        for j in range(iterations):
            for q in range(3):
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i + q, color)
                self.strip.show()
                time.sleep(wait_ms / 1000.0)
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i + q, 0)

    def __colorStatic(self, color, wait_ms=0):
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, color)
            self.strip.show()
            time.sleep(wait_ms / 1000.0)
    
    def __colorFlash(self, color, wait_ms=100):
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, color)
            self.strip.show()
        time.sleep(wait_ms / 1000.0)
        self.clear()
