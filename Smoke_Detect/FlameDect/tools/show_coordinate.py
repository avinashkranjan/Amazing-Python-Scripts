#! /usr/bin/env python
# coding=utf-8
import cv2

help_message = '''
*******************************INFO************************************
USAGE: click.py <image_names> ...

Click the picture show the coordinate and BGR value of the point, ESC to stop.
*****************************INFO_END**********************************
'''

default_img_src = '/home/stone/Pictures/extractFrames/frame600.jpg'


def coordinate(event, x, y, flags, para):
    if event == cv2.EVENT_LBUTTONUP:
        print "*" * 20
        print 'Coordinate: %s' % [x, y]
        print 'BGR: %s' % img[x][y]


if __name__ == '__main__':
    import sys

    print help_message

    try:
        img_src = sys.argv[1]
    except:
        img_src = default_img_src

    img = cv2.imread(img_src)

    if img is None:
        print 'please input the right order !!!\n'
    else:
        width, height, r = img.shape
        print "size of the picture: {}*{}px".format(width, height)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', coordinate)

        while True:
            cv2.imshow('image', img)
            if cv2.waitKey(0) & 0xFF == 27:
                break
            else:
                continue

    cv2.destroyAllWindows()
