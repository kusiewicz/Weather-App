# Download icons images.

import os

import urllib.request 

day = ["01d@2x.png", "02d@2x.png", "03d@2x.png", "04d@2x.png", "09d@2x.png", "10d@2x.png", "11d@2x.png","13d@2x.png", "50d@2x.png"]
night = ["01n@2x.png", "02n@2x.png", "03n@2x.png", "04n@2x.png", "09n@2x.png", "10n@2x.png", "11n@2x.png","13n@2x.png", "50n@2x.png"]

base_url = " http://openweathermap.org/img/wn/"
img_dir = "./icons/"

if not os.path.exists(img_dir):
    os.makedirs(img_dir)

# Get the day weather icons
for name in day:
    file_name = img_dir+name
    urllib.request.urlretrieve(base_url+name, file_name)

# Get the night weather icons
for name in night:
    file_name = img_dir+name 
    urllib.request.urlretrieve(base_url+name, file_name)


