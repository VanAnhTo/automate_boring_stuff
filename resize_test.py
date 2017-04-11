import cv2
import os

path = "input/eng"
resize_path = "input"
dirs = os.listdir( path )

img_counter = 0
for img in dirs:
    #print (image)
    image = cv2.imread(path +"/" + img)
    cv2.imshow("original", image)
    print (image.shape)
    
    r = 800.0 / image.shape[1]
    dim = (800, int(image.shape[0] * r))

    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow("resized", resized)

    picName = resize_path + "/" + 'pic_resize_{}.png'.format(img_counter)
    cv2.imwrite(picName, resized)
    img_counter += 1
    
cv2.waitKey(0)

