#!/usr/bin/env/python

# Import os for raspistill, 
import os
import base64
import time
from PIL import Image

# Import library and create instance of REST client.
from Adafruit_IO import Client

#post to Adafruit.io account
aio = Client('YOUR_CLIENT_KEY')

# Capture image with raspistill
#os.system("raspistill -o -q 50 image.jpg")
os.system("raspistill -w 640 -h 480 -n -q 5 -o image.jpg")

time.sleep(5)

photosPath = '/home/pi/picamera/'
photoFile = 'image.jpg'

# Get the name for the thumbnail file
thumbnailFileName = 'thumb_' + photoFile

# Make the thumbnail file
with open(photosPath + photoFile, 'rb') as fd_img:
    img = Image.open(fd_img)
    size = 640, 480
    img.thumbnail(size)
    img.save(photosPath + thumbnailFileName, img.format)
    fd_img.close()

# Encode the file to a base64 string
with open(photosPath + thumbnailFileName, "rb") as f:
    imgData = base64.b64encode(f.read()).decode()

    f.close()

# Send image to ImageFeed feed
aio.send('ImageFeed', imgData)
