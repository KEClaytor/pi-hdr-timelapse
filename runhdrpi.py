#! /usr/bin/python
# Main script for running the HDR capture-merge sequence
from capturehdr import *
from mergehdr import *
from time import sleep
from datetime import datetime
from subprocess import call

if __name__=="__main__":
    # Options for timelapse
    nimages = 10 #2160
    delay = 10
    basename = 'image'
    datestring = datetime.now().__format__('%Y-%m-%d_%I%p')
    timelapsename = '%s.mp4' % (datestring)
    # Options for capture
    emin = 10
    emax = 90
    nexp = 5
    w = 800
    h = 600
    # Options for merging
    # nothing yet
    # Options for ffmpeg
    # nothing yet

    # Log file
    f = open('hdrpi.log', 'a')
    f.write('Starting HDR sequence.\n')
    f.write('Current Time: ' + datetime.now().isoformat())

    # Initalize camera and set resolution
    camera = InitalizeCamera()
    camera.resolution = (w, h)
    f.write('Initialized Camera.\n')

    
    # Capture our images
    for ii in range(nimages):
        images = CaptureHDRStack(camera, emin, emax, nexp)
        WriteResponseFile(images)
        f.write('Captured HDR Stack.\n')
        # Merge them into an HDR image
        imgname = '%s_%04d.jpg' % (basename, ii + 1)
        MergeHDRStack(imgname)
        f.write('Merged HDR Stack.\n')
        sleep(delay)

    # Create the time lapse
    call(["avconv", "-r", "10", "-i", "%s_%04d.jpg" % (basename), "-vcodec", "libx264", "-crf",  "20", "-g", "15", timelapsename])
    f.write('Wrote video\n.')
    f.write('Current Time: ' + datetime.now().isoformat())
