import cv2
import os
import math

img = "input/eng/IMG_2460.JPG"
resize_path = "input"

image = cv2.imread(img)
cv2.imshow("original", image)

or_size = os.stat(img).st_size
print('Original size:'+ str(or_size))

r = 450/image.shape[1]

dim = (450, int(image.shape[0] * r))


print ( 'r ' + str(r))
print ('dim' + str(dim))


resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

cv2.imshow("resized", resized)
#print( resized.shape)


picName = resize_path + "/" + 'pic_resize_a.png'
cv2.imwrite(picName, resized)

print(('New size: ')+ str(os.path.getsize(picName))+ '\n')
