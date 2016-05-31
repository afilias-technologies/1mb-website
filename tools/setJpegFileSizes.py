#! /usr/bin/python

from subprocess import call
from random import randrange
import sys, os


def randomBytes(length):
    bytes = ''
    for i in range(0,length):
        bytes += chr(randrange(32, 125))
    return bytes


def getFileSize(filePath):
    return os.path.getsize(filePath)


def sumFileSizes(files):
    total = 0
    for filePath in files:
        total += getFileSize(filePath)
    return total


def setExifComment(filePath, comment):
    result = call(['exiftool', '-comment=' + comment[:-4], os.getcwd() + '/' + filePath])
    return True if result == 0 else False


def clearExifComment(filePath):
    result = call(['exiftool', '-comment=', os.getcwd() + '/' + filePath])
    return True if result == 0 else False


def main():
    if len(sys.argv) < 3:
        print os.path.basename(__file__) + ' <JPEG images> <desired bytesize delta>'
        print 'Note that JPEGs may need to have comments stripped first to ensure correct result e.g. "exiftool -comment= *.jpg"'
        sys.exit(0)

    sourceFiles = sys.argv[1:-1]
    oldSize = sumFileSizes(sourceFiles)

    print 'Source files: %s' % ' '.join(sourceFiles)
    print 'Total size of files is %d bytes\n' % oldSize
    delta = int(sys.argv[-1])

    if delta/len(sourceFiles) > 64000:
        print 'Target file size not reachable (%d byte delta required)' % delta
        print 'Adding %d JPEG(s) will make target reachable' % ( int((delta - len(sourceFiles) * 64000)/64000)+1)
        sys.exit(0)
    elif delta < 0:
        print 'Desired size less than existing size (%d byte delta)' % delta
        sys.exit(0)
    else:
        print 'Adding %d bytes over %d files' % (delta, len(sourceFiles))


    perFileDelta = int(delta / len(sourceFiles))
    print '  Per file increase is %d' % perFileDelta

    for filePath in sourceFiles[0:-1]:
        print '    adding %d bytes to %s' % (perFileDelta, filePath)
        clearExifComment(filePath)
        setExifComment(filePath, randomBytes(perFileDelta))

    remainder = delta - len(sourceFiles[:-1]) * perFileDelta
    print '    adding %d bytes to %s' % (remainder, sourceFiles[-1])
    clearExifComment(sourceFiles[-1])
    setExifComment(sourceFiles[-1], randomBytes(remainder))

    newSize = sumFileSizes(sourceFiles)
    print '\nNew total size is %d bytes (%d bytes increase)' % (newSize, newSize - oldSize)


if __name__ == '__main__':
    main()
