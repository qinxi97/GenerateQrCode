#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2023/12/21 17:03
# file: Genrator_qrcode.py
# author: qinxi
# email: 1023495336@qq.com

import random
import string
import pyqrcode, png
from pyqrcode import QRCode

#  pip3 install pyqrcode
#  pip3 install pypng

def generate_randon_name(len=12):
    """Generate a random name consisting or letters and digits."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=len))

text_to_convert = input("Enter text to convert: ")

# Creating QR code after given text "input"
url = pyqrcode.create(text_to_convert)

# Saving QR code as a png file
url.show()

# Asking for the image name to save
image_name_input = input("Enter image name to save (leave blank for a random name): ")
if not image_name_input:
    image_name = generate_randon_name()
else:
    image_name = image_name_input

# Name of QR code png file "input"
url.png(image_name + ".png", scale=6)


