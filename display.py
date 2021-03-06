#interface between jgarff's neopixel dma python lib and brainsmoke's fire animation.
#BrettRD 2018

from time import sleep
from fire import Fire
from neopixel import *

cols=24
rows=45

# LED strip configuration:
LED_COUNT      = rows*cols      # Number of LED pixels.
LED_PIN        = 10      # GPIO pin connected to the pixels.
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
LED_STRIP      = ws.SK6812_STRIP_GRBW

sim = Fire(cols,rows)

# Main program logic follows:
if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    try:
        while True:
            #step the animation
            image = sim.next()
            for col in range(0, cols):
                for row in range(0, rows):
                    #assign channels of the image to leds
                    red = image[row][col][0]
                    green = image[row][col][1]
                    blue = image[row][col][2]
                    strip.setPixelColor((col*rows) + row, Color(red,green,blue))
            strip.show()
            #sleep(0.02)


    except KeyboardInterrupt:
        #clean up
        for j in range(strip.numPixels()):
            strip.setPixelColor(j, Color(0,0,0))
        strip.show()
        exit(1)
