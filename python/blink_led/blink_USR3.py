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

User will blink the LED at x Hz/second

--------------------------------------------------------------------------
"""
# NOTE - Add import statements to allow access to Python library functions
import Adafruit_BBIO.GPIO as GPIO
import time
# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

# NOTE - No constants are needed for this example 

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# NOTE - Need a global variable to map an operator string (e.g. "+") to 
# NOTE - the appropriate function.


# ------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------

# NOTE - Add function "get_user_input()".  This function will:
# NOTE -     """Get input from the user.
# NOTE -          Returns tuple:  (number, number, function) or
# NOTE -          (None, None, None) if inputs invalid
# NOTE -     """
# NOTE - 
# NOTE - User input is generally returned as a string and must be translated.

# End def


# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

# NOTE - The python variable "__name__" is provided by the language and can 
# NOTE - be used to determine how the file is being executed.  For example,
# NOTE - if the program is being executed on the command line:
# NOTE -   python3 simple_calc.py
# NOTE - then the "__name__" will be the string:  "__main__".  If the file 
# NOTE - is being imported into another python file:
# NOTE -   import simple_calc
# NOTE - the the "__name__" will be the module name, i.e. the string "simple_calc"
