pi-hdr-timelapse
================

Python scripts for capturing and merging HDR images on the Raspberry Pi and stringing them into a timelapse.


Installation
------------
You'll need [picamera](https://pypi.python.org/pypi/picamera/) [git source](https://github.com/waveform80/picamera/) and [enblend/enfuse](http://enblend.sourceforge.net/).
```
sudo apt-get update
sudo apt-get install python-picamera enblend
```
Then grab these files;
```
git clone https://github.com/KEClaytor/pi-hdr-timelapse.git
```
You should be good to go! Edit the first few lines of runhdrpi.py to your liking (exposure steps, time lapse steps) and go;
```
nano runhdrpi.py
python runhdrpi.py
```

Scheduled Run
-------------
You can also schedule timelapse images with cron (eg. for morning / afternoon timelapse).

_section coming_
