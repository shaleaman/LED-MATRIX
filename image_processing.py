from numpy import *
from PIL import Image
from PIL import GifImagePlugin
from noise import pnoise1
import os
import time

from neopixel import *

import argparse
import signal
import sys


def signal_handler(signal, frame):
        colorWipe(strip, Color(0,0,0))
        sys.exit(0)

# def opt_parse():
#         parser = argparse.ArgumentParser()
#         parser.add_argument('-c', action='store_true', help='clear the display on exit')
#         args = parser.parse_args()
#         if args.c:
#                 signal.signal(signal.SIGINT, signal_handler)

# LED strip configuration:
LED_COUNT      = 192    # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10   # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_RGB   # Strip type and colour ordering

speed = .05 # frame time for gif animation
w = 12 # width of pixel matrix
h = 16   # height of pixel matrix
img_rgb_matrix = [[[] for x in range(h)] for y in range(w)] # construct matrix to hold rgb vals

image_name = sys.argv[1]

print(image_name)

def display_img(strip, matrix):
    for i in range(h):
        for j in range(w):
            led_index = (w*h)- 1 - int(i*w+j)
            color = matrix[j][i]
            strip.setPixelColor(led_index, Color(*color))
    strip.show()

def sample_image(img):
    for i in range(h):                               #iterate through rows
            for j in range(w):                           # iterate through columns
                img_x = j
                if i%2 == 0:
                    img_x = (w-1)-j
                img_rgb_matrix[j][i] = img[img_x,i]   # load matrix with rgb values
    return(img_rgb_matrix)

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    #opt_parse()
    counter = 0
    is_gif = False # Test to see if image is animated
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    img = Image.open("images/"+image_name)# Open Image to Display
    img = img.resize((w,h),Image.ANTIALIAS)        # Resize and downsample image to matrix dimensions
    img = img.rotate(-90)
    img.show(title="TEST")
    img_loaded = img.load()
    img_rgb_matrix = sample_image(img_loaded)
    #print(img_rgb_matrix)
    display_img(strip, img_rgb_matrix)#print(array(img)))
