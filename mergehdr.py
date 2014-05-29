# A script for merging the HDR stack using enblend / enfuse
from subprocess import call
from datetime import datetime

def MergeHDRStack():
    """MergeHDRStack(fnames)
        Merge the files contained in fnames using enfuse.
        options are passed to enfuse.
    """
    # Create a formated date for the file name
    ctime = datetime.now().__format__('%Y-%m-%dT%H:%M:%S')
    outfile = '--output=%s.jpg' % (ctime)
    call(["enfuse", outfile, "@hdrstack"])
    return True

