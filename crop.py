import cv2
import os
import datetime
import shutil

path = "input_crop"
dirs = os.listdir( path )
cropped = "backup_cropped"

def new_file_name():
    now = datetime.datetime.now()
    new_file_name = now.strftime("%Y%m%d_%H%M%S%f"+ ".png")
    return new_file_name

def save_file(str):
    new_file = cropped +"/" + new_file_name()
    cv2.imwrite(new_file, str)
    return

for im in dirs:
    img = path + "/" + im
    img = cv2.imread(img)
    #cv2.imshow("cropped", img)

    # Crop from x, y, w, h -> 100, 200, 300, 400
    # NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]

    height, width, channels = img.shape
    print (height, width, channels)


    title = img[0:800, 0:width]
    save_file(title)

    rate = height//5

    menu = img[height-rate:height, 0:width]
    save_file(menu)

    content = img[rate:height -rate , 0:width]

    haft = width//2

    haft_content_left = img[rate:height - rate, 0 : haft ]
    save_file(haft_content_left)

    haft_content_right = img[rate:height - rate, haft : width ]
    save_file(haft_content_right)

    '''title_gray = cv2.cvtColor(title, cv2.COLOR_BGR2GRAY)
    menu_gray = cv2.cvtColor(menu, cv2.COLOR_BGR2GRAY)'
    cv2.imshow("cropped", haft_content_left)
    #cv2.imshow("cropped", menu_gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''




