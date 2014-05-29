# A script for merging the HDR stack using enblend / enfuse
from subprocess import call
from datetime import datetime

def MergeHDRStack(image_name=None):
    """MergeHDRStack(fnames)
        Merge the files contained in fnames using enfuse.
        options are passed to enfuse.
    """
    if image_name is None:
        now = datetime.now()
        # Create a formated date for the file name
        date = now.__format__('%Y-%m-%d')
        seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
        minutes = int(seconds_since_midnight/60)
        image_name = '%sT%04d.jpg' % (date, minutes)
    
    outfile = '--output=%s' % (image_name)

    call(["enfuse", outfile, "@hdrstack"])
    print "wrote file %s" % (image_name)
    return True

if __name__=="__main__":
    pass
