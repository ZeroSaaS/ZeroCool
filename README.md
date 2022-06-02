ZeroCool.py 
Script for pulling temperature values from thermocouple connected to a Pi Zero W and posting data to Adafruit IoT dashboard.

PiCamera.py
Python script for taking camera images and posting to Adafruit.io dashboard. 

Add these python scripts to crontab so they automatically run when you connect the Pi to power. 
Add a line in your crontab file to run these python scripts 60 seconds after startup
Add a second line in your crontab file to run these python scripts however frequently you prefer. 
