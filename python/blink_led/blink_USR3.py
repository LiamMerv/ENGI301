# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Blink LED
--------------------------------------------------------------------------
License:   
Copyright 2022 - Liam Merva

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Program that will
    - Blink USR3 LED at a 5 Hertz frequency

Operation:
    - LED On/Off Cycling (5 full on/off cycles per second)

No error conditions are present in this code

--------------------------------------------------------------------------
"""
# NOTE - Add import statements to allow access to Python library functions
import Adafruit_BBIO.GPIO as GPIO
import time
# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

# NOTE - No constants are needed 

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------
#Establishes LED target on PocketBeagle
LEDs = ["USR3"]
delay = 0.2
# ------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------
#Turns LED on/off based on the cycles dictated by the delay variable
for LED in LEDs:
    print(LED)
    GPIO.setup(LED, GPIO.OUT)

while True:
    for LED in LEDs:
        GPIO.output(LED, 1)
    time.sleep(delay)
    for LED in LEDs:
        GPIO.output(LED, 0)
    time.sleep(delay)

# End def


# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------
#No Main script is necessary for this program