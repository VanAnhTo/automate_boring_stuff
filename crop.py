import cv2
import os
import datetime
import shutil

path = "screen_capture"
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

for image_name in dirs:
    img_path = path + "/" + image_name
    img = cv2.imread(img_path)
    print(image_name)

    temp = image_name.split("_")

    image_type = temp[len(temp)-1]
    
    image_type = os.path.splitext(image_type)[0]
    
    print(image_type)


    height, width, channels = img.shape
    print (height, width, channels)
    rate = height//5

    if (image_type == 'popup'): 

        popup = img[height//5:(4*height)//5 , width//6: (5*width)//6]
        save_file(popup)
            
        popup_title = img[450: 770 , width//6: (5*width)//6]
        save_file(popup_title)

        popup_content = img[770:1560 , width//6: (5*width)//6]
        save_file(popup_content)

        popup_button = img[1560:1990 , width//6: (5*width)//6]
        save_file(popup_button)

    if (image_type == 'line'):
        line3 = img[(3*height)//7:(4*height)//7, 0: width]
        save_file(line3)
            
        line4 = img[(4*height)//7:(5*height)//7, 0: width]
        save_file(line4)

        line5 = img[(5*height)//7:(6*height)//7 , 0: width]
        save_file(line5)

        line6 = img[(6*height)//7:height , 0: width]
        save_file(line6)

    if (image_type == 'divide'):
        
        content = img[rate:height -rate , 0:width]

        haft = 2* width//5

        haft_content_left = img[rate : height - rate, 0 : haft ]
        save_file(haft_content_left)

        haft_content_right = img[rate:height - rate, haft : width ]
        save_file(haft_content_right)
    

    '''title_gray = cv2.cvtColor(title, cv2.COLOR_BGR2GRAY)
    menu_gray = cv2.cvtColor(menu, cv2.COLOR_BGR2GRAY)'
    cv2.imshow("cropped", haft_content_left)
    #cv2.imshow("cropped", menu_gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''




