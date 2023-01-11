# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Automatic Plant Watering System
--------------------------------------------------------------------------
License:   
Copyright 2022-2023 Liam Merva
Based on library from
Copyright 2018 Nicholas Lester
Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------
Software API:
    
    * Adafruit Circuit Python
        * used to interface ILI9341 LCD Screen with PocketBeagle
    * Adafruit_Blinka
        * used for circuit python to then use digitalio
  
--------------------------------------------------------------------------
Background Information: 
 
    * Base code/instructions for Display:
        * https://github.com/adafruit/Adafruit_CircuitPython_Bitmap_Font/
--------------------------------------------------------------------------
Outline:
    - Set up PocketBeagle, LCD Screen, Humidity Sensor, Light Sensor, and Water Delivery System (Pump)
    - Create LCD Display to Show Relative Humidity and Light Levels
    - Use functions to gather relevant humidity and light data in microenvironment surrounding plant
        - Deliver water when soil humidity falls below target threshold value
        - Activate light bulb when light levels fall below target threshold value
        
"""
#import os
#import digitalio
#import board
#from board import SCL, SDA
#import busio
#from PIL import Image
#from PIL import ImageDraw
#from PIL import ImageFont
#import displayio
#import adafruit_ili9341
#import Adafruit_BBIO.SPI as SPI
#import terminalio
#import adafruit_display_text
#from adafruit_display_text import label
#from adafruit_bitmap_font import bitmap_font
import time
import random

#from adafruit_bitmap_font import bitmap_font
#from displayio import Bitmap
#Import necessary libraries for light sensors

#import Adafruit_BBIO.GPIO as GPIO
#import Adafruit_BBIO.ADC as ADC
#import Adafruit_BBIO.PWM as PWM

#Import necessary libraries for soil humidity sensor

#from adafruit_seesaw.seesaw import Seesaw
#i2c_bus = busio.I2C(SCL, SDA)

#Set up LCD Display SPI Bus

#from Adafruit_BBIO.SPI import SPI
#spi = board.SPI()
# ------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------
  
def soilcheck(species):
    """
    Uses soil moisture sensor to get reading of moisture and designates whether moisture is at adequate or inadequate level
    """
    #i2c_bus = busio.I2C(SCL, SDA)
    #import Adafruit_BBIO.ADC as ADC
    #import Adafruit_BBIO.PWM as PWM
    #ss = Seesaw(i2c_bus, addr=0x36)
    pump_pin = "P2_3"
    # theoretically read moisture level through capacitive touch pad
    #touch = ss.moisture_read()
    touch = random.randint(200, 1000)
    if species == 'flowering':
        if touch < 500:
            #PWM.start(pump_pin)
            print('Pump is on')
        else:
            #PWM.stop(pump_pin)
            print('Pump is off')
    elif species == 'foliage':
        if touch < 750:
            #PWM.start(pump_pin)
            print('Pump is on')
        else:
            #PWM.stop(pump_pin)
            print('Pump is off')
    #print("Moisture Level: " + str(water))
    print("Moisture Level: " + str(touch))
    return(touch)
    
def lightcheck():
    """
    Uses both light sensors to get voltage reading, then averages them to categorize light level 
    If light level is below necessary level, LED turns on (ex. it is nighttime)
    If light level is above necessary level, LED turns off (ex. it is daytime)
    """
    #import Adafruit_BBIO.ADC as ADC
    #import Adafruit_BBIO.PWM as PWM
    analog_in_1="P1_19"
    analog_in_2="P1_21"
    LED_pin = "P2_4"
    #ADC.setup()
    #value1 = ADC.read_raw(analog_in_1)
    #value2 = ADC.read_raw(analog_in_2)
    value1 = random.randint(1800, 2200)
    value2 = random.randint(1700, 2300)
    avgvalue = (value1 + value2)/2
    if avgvalue < 2000:
        #PWM.start(LED_pin)
        print('LED is on')
    else:
        #PWM.stop(LED_pin)
        print('LED is off')
    print("Light Level: " + str(avgvalue))
    return(avgvalue)

def displaymoistureandlight(string):
    """
    Displays 
    """
    #spi = board.SPI()
    #tft_cs = board.P2_2
    # Create the display
    #displayio.release_displays()
    #display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs)
    
    #display = adafruit_ili9341.ILI9341(display_bus, width=320, height=240)
    #splash = displayio.Group(max_size=10)
    #display.show(splash)
    
    #color_bitmap = displayio.Bitmap(320, 240, 1)
    #color_palette = displayio.Palette(1)
    #color_palette[0] = 0x339933
    #bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
    #splash.append(bg_sprite)
    #font = bitmap_font.load_font("Helvetica-Bold-16.bdf")
    #color = 0xFFFFFF
    #text_area = label.Label(font, text=string, color=color)
    #text_area.x = 75
    #text_area.y = 70
    #splash.append(text_area)
    #while True:
        #pass
        
def executedisplay():
    moisture = soilcheck()
    light = lightcheck()
    string = "Moisture Level: " + str(moisture) + "Ambient Light Level: " + str(light)
    displaymoistureandlight(string)

#-------------------------------------------------------------------------------
# Main Script
#-------------------------------------------------------------------------------

if __name__ == '__main__':
    print("What species of plant are you raising? For flowering plant, type 'flowering'. For foilage plant, type 'foliage')")
    species = input("What species of plant: ")
    if species == 'flowering' or species == 'foliage':
        while True:
            soilcheck(species)
            lightcheck()
            time.sleep(3)
    else:
        print("Not a valid input - program will not be run")
    
    