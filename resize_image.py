import cv2
import os
import math

path = "input/eng"
resize_path = "input"
dirs = os.listdir( path )

img_counter = 0
for img in dirs:
    image = cv2.imread(path +"/" + img)
    cv2.imshow("original", image)
    print ('Previous size: ' + str(os.stat(path +"/" + img).st_size))
    
    r = 450 / image.shape[1]
    print ( 'r ' + str(r))
    dim = (450, int(image.shape[0] * r))
    print ('dim' + str(dim))

    '''
    #resize with fix height = 100
    
    r = 100/image.shape[0]
    dim = (int(image.shape[1]*r) , 100)
    resized = cv2.resize(image,dim,interpolation = cv2.INTER_AREA)'''

    #Resize the image with new high and weight
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow("resized", resized)
    print(resized.shape)

    #Save as new image base after resize the image
    picName = resize_path + "/" + 'pic_resize_{}.png'.format(img_counter)
    cv2.imwrite(picName, resized)
    print(('New size: ')+ str(os.path.getsize(picName))+ '\n')
    
    img_counter += 1
    
cv2.waitKey(0)

