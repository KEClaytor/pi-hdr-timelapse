# Main script for running the HDR capture-merge sequence
from capturehdr import *
from mergehdr import *
from time import sleep
from datetime import datetime
from subprocess import call

if __name__=="__main__":
    # Options for timelapse
    nimages = 180
    delay = 60
    basename = 'image'
    datestring = datetime.now().__format__('%Y-%m-%d')
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

    # Initalize camera and set resolution
    camera = InitalizeCamera()
    camera.resolution = (w, h)

    # Capture our images
    for ii in range(nimages):
        images = CaptureHDRStack(camera, emin, emax, nexp)
        WriteResponseFile(images)
        # Merge them into an HDR image
        imgname = '%s_%04d.jpg' % (basename, ii + 1)
        MergeHDRStack(imgname)
        sleep(delay)

    # Create the time lapse
    call(["avconv", "-r", "10", "-i", "%s_%%04d.jpg" % (basename), "-r", "10","-vcodec", "libx264","-crf",  "20", "-g", "15", timelapsename])
