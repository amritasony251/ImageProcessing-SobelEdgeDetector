import cv2
import numpy as np
from PIL import Image

img = cv2.imread("girl.png")
height, width, depth = np.shape(img)

ver = [[-1,0,1],
       [-2,0,2],
       [-1,0,1]]
       
hor = [[-1,-2,-1],
       [0, 0, 0],
       [1,2,1]]
                         
       
H = int(len(ver))

for i in range(0, height-H):
    for j in range(0, width-H):
        summ = 0
        for k in range(0, H):
            for l in range(0, H):
                summ = summ + ver[k][l]*img[i+k][j+l]  #ver for vertical edge detection
        if(summ[0]>255):
           summ = [255,255,255]
        elif(summ[0]<0):
           summ = [0,0,0]          
        img[i][j] = summ  
            

cv2.imshow('image',img)
cv2.waitKey(0)               
