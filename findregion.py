import cv2
import numpy as np
from image import Image
# this will input a canny image
# log locations of pixels with a given color
# then, take a walk around the graph of connected pixels

class ImageRegion(object):
    def __init__(self,image,thresh1, thresh2):
        bf = image.read_bright_field()
        gfp = image.read_gfp()

        cannybf = cv2.Canny(bf,thresh1,thresh2)
        cannygfp = cv2.Canny(gfp,thresh1, thresh2)

        self.image = Image(cannybf,cannygfp)
    
    def get_contours(self):
        # find contours
        _, contoursbf, _ = cv2.findContours(self.image.read_bright_field(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        _, contoursgfp, _ = cv2.findContours(self.image.read_gfp(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        return (contoursbf, contoursgfp)