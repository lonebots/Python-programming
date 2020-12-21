#area estimation of the states in India
#using the
#computing the area with random trials given

#increase the number of iterations

import numpy as np
from PIL import Image

#create image of particular rgb values
width = 5
height = 4
array = np.zeros([height, width, 3], dtype=np.uint8)
#zeros make array m*n , 3 represent values for rgb byte value, dtype of datatype unsigned int

img = Image.fromarray(array)
img.save('test.png')

array1 = np.zeros([100, 100, 3], dtype=np.uint8)
array1[:, :50] = [255, 128, 0]  #orange color
array1[:, 50:] = [0, 0, 255]  #blue
img = Image.fromarray(array1)
img.save('test1.png')
