# Main script for running the HDR capture-merge sequence
from capturehdr import *
from mergehdr import *

if __name__=="__main__":
    # Options for capture
    emin = 10
    emax = 90
    nexp = 4
    # Options for merging
    # nothing yet
    # Options for ffmpeg
    # nothing yet

    # First capture our images
    camera = InitalizeCamera()
    images = CaptureHDRStack(camera, emin, emax, nexp)
    WriteResponseFile(images)
    # Merge them into an HDR image
    MergeHDRStack()

