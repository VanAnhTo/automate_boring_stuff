

# import the necessary packages
import cv2

path = "input/eng"
 
# load the image and show it



image = cv2.imread(path + "/" + "opencv_frame_0.png")
cv2.imshow("original", image)
r = 100.0 / image.shape[1]
dim = (100, int(image.shape[0] * r))

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("resized", resized)

print (image.shape)


cv2.waitKey(0)

