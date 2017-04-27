import cv2
import os
import math

img = "input/eng/IMG_1586.JPG"
resize_path = "input"

image = cv2.imread(img)
cv2.imshow("original", image)

or_size = os.stat(img).st_size
print('Original size:'+ str(or_size))

x = math.sqrt(or_size/512000)
new_w = int(image.shape[0]/x)
new_h = int (image.shape[1]/x)

dst = cv2.resize(image, (new_w, new_h), interpolation = cv2.INTER_CUBIC)

cv2.imshow("resized", dst)
#print( resized.shape)


picName = resize_path + "/" + 'pic_resize_a.png'
cv2.imwrite(picName, dst)

'''
new_w = int(image.shape[0]/x)
new_h = int (image.shape[1]/x)


r = 500/new_h

dim = (500, int(new_h * r))


print ( 'r ' + str(r))
print ('dim' + str(dim))


resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

cv2.imshow("resized", resized)
#print( resized.shape)


picName = resize_path + "/" + 'pic_resize_a.png'
cv2.imwrite(picName, resized)'''

print(('New size: ')+ str(os.path.getsize(picName))+ '\n')
