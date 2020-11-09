from numpy import genfromtxt
import numpy as np
from PIL import Image
weight,height = 960,540
canvas = np.zeros((height,weight,3), dtype=np.uint8)
image = genfromtxt('DS2.txt',dtype='int')
for i in range(540):
    for j in range(960):
        canvas[i][j] = [255,255,255]
for i in range(34096):
    for j in range(2):
        if(j==0):
            x = image[i][j]
        elif(j == 1):
            y = image[i][j]
    canvas[x][y] = [0,0,0]
a = Image.fromarray(canvas,'RGB')
a.save('Lab№2.jpg')
a.show()