import cv2
import os
import math

img = "input/eng/IMG_1586.JPG"
resize_path = "input"

or_size = os.stat(img).st_size
print('Original size:'+ str(or_size))

x = math.sqrt(or_size/512000)

image = cv2.imread(img)
cv2.imshow("original", image)

small = cv2.resize(image, (1000, 1500)) 
#small = cv2.resize(image, (0,0), fx= x, fy = x)
cv2.imshow("resized", small)
   
picName = resize_path + "/" + 'pic_resize_a.png'
cv2.imwrite(picName, small)

print(('New size: ')+ str(os.path.getsize(picName))+ '\n')
