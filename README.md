pi-hdr-timelapse
================

Python scripts for capturing and merging HDR images on the Raspberry Pi and stringing them into a timelapse.


Installation
------------
You'll need [picamera](https://pypi.python.org/pypi/picamera/) ([git source](https://github.com/waveform80/picamera/)) for managing the camera, [enblend/enfuse](http://enblend.sourceforge.net/) to generate the HDR images and [avconv](https://libav.org/avconv.html) to generate the movie from the images.
```
sudo apt-get update
sudo apt-get install python-picamera enblend libav-tools
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
You can also schedule timelapse images with cron (eg. for morning / afternoon timelapse). Make sure that the first line of runhdrpi.py points to your python install. Then just add the following line to your crontab (run `crontab -e`):

```
0 5,20 * * * /home/pi/path-to-script/runhdrpi.py >> /home/pi/path-to-log/runhdrpi.log
```
The above will run the script at 5 AM and 8 PM every day.

**Note:** It seems as though the pi's cron is a bit pecular about time zones. For instance, it _should_ use the local time, however, I find mine only uses UTC ([it seems like others have this problem too](http://www.raspberrypi.org/forums/viewtopic.php?t=70809&p=514956)). So you may have to make allowances for that.
