# nick nazari
# may 1 2019
# create grid of boxes
import cv2
import numpy as np
import random

pixelwidth = 512
img = np.zeros((pixelwidth,pixelwidth,3), np.uint8)

# we can define size n as n x n grid of squares
length = 128

increment = pixelwidth // length

def randomColor():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

startnums = []
for i in range(0, length):
    startnums.append(i * (pixelwidth // length))

starters = [(x,y) for x in startnums for y in startnums]
print(starters)

for start in starters:
    cv2.rectangle(img, start, (start[0] + increment, start[1] + increment), randomColor(), -1)

cv2.imshow('grid', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
