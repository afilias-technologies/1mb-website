from subprocess import call
from random import randrange
import sys, os


def randomBytes(length):
    bytes = ''
    for i in range(0,length):
        bytes += chr(randrange(32, 125))
    return bytes


def main():
    if len(sys.argv) != 3:
        print os.path.basename(__file__) + ' <JPEG image> <desired bytesize>'
        sys.exit(0)

    sourceFile = sys.argv[1]
    currentSize = os.path.getsize(sourceFile)

    # clear existing comment
    call(['exiftool', '-comment=', sourceFile])

    desiredSize = int(sys.argv[2])
    delta = desiredSize - currentSize
    print 'The current file size is %d bytes' % currentSize

    if delta > 64000:
        print 'Desired size not reachable (%d byte delta)' % delta
        sys.exit(0)
    elif delta < 0:
        print 'Desired size less than existing size (%d byte delta)' % delta
        sys.exit(0)
    else:
        print 'Adding %d bytes to file' % delta


    # set new comment
    call(['exiftool', '-comment=' + randomBytes(delta-4), sourceFile])

if __name__ == '__main__':
    main()
