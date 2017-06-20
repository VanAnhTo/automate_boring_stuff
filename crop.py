import cv2


img = cv2.imread("2222.png")
#cv2.imshow("cropped", img)
height, width, channels = img.shape
print (height, width, channels)
title = img[0:150, 0:width]
cv2.imwrite("title.png",title)

rate = height//5

menu = img[height-rate:height, 0:width]

cv2.imwrite("menu.png",menu)
# Crop from x, y, w, h -> 100, 200, 300, 400
# NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]

content = img[rate:height -rate , 0:width]

haft = width//2

haft_content_left = img[rate:height - rate, 0 : haft ]
cv2.imwrite("haft_content_left.png",haft_content_left)

haft_content_right = img[rate:height - rate, haft : width ]
cv2.imwrite("haft_content_right.png",haft_content_right)


'''title_gray = cv2.cvtColor(title, cv2.COLOR_BGR2GRAY)
menu_gray = cv2.cvtColor(menu, cv2.COLOR_BGR2GRAY)'


cv2.imshow("cropped", haft_content_left)

#cv2.imshow("cropped", menu_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()'''
