# nick nazari
# may 1 2019
# grid object to make grid of boxes

import cv2
import numpy as np
import random
import time

class Grid:
    def __init__(self, pixelwidth, length):
        self.pixelwidth = pixelwidth
        self.length = length  
        self.increment = pixelwidth // length
        self.img = np.zeros((pixelwidth, pixelwidth, 3), np.uint8)

        # defining start positions
        startnums = []
        for i in range(0,length):
            startnums.append(i * (pixelwidth // length))

        self.starters = [(x,y) for x in startnums for y in startnums]

    def clear(self):
        self.img = np.zeros((self.pixelwidth, self.pixelwidth, 3), np.uint8)
        
    def show(self):
        cv2.imshow('Grid', self.img)

        # configuring click event handler function
        def clickHandler(event, x, y, flags, params):
            if event == cv2.EVENT_LBUTTONDOWN:
                print(x//self.increment,y//self.increment)
                self.set(x//self.increment, y//self.increment, 0,0,255)
                self.show()

        cv2.setMouseCallback('Grid', clickHandler)

        cv2.waitKey(0)

    def kill(self):
        cv2.destroyAllWindows()

    # set a square to a color
    def set(self, x, y, b, g, r):
        basex = x*self.increment
        basey = y*self.increment
        cv2.rectangle(self.img, (basex, basey), (basex + self.increment, basey + self.increment), (b,g,r), -1)

    def get(self, x, y):
        # add this method to get color at a position
        return self.img[x*self.increment,y*self.increment]

    def randomColor(self):
        return (random.randint(0,255),random.randint(0,255),random.randint(0,255)) 

    def randomFill(self):
        for start in self.starters:
            cv2.rectangle(self.img, start, (start[0] + self.increment, start[1] + self.increment), self.randomColor(), -1)


if __name__ == "__main__":
    bad = [0,0,255]
    good = [0,255,0]
    mygrid = Grid(512, 4)
    mygrid.set(1,1,*bad)
    mygrid.set(1,3,*good)
    mygrid.set(0,0,*good)
    print(mygrid.get(0,0))
    mygrid.show()
