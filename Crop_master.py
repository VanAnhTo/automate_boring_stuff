from common import new_file_name
from common import save_file
import cv2
import os
import datetime
import shutil

path = "input_crop"

dirs = os.listdir( path )
cropped = "backup_cropped/"

input_line = "input_line"
input_popup = "input_popup"
input_divide_screen = "input_divide_screen"

for folder in dirs:
    #folder_name = folder    
    print(folder)
    files = os.listdir( path + "/" + folder )
    
    for im in files:
        img = path + "/" + folder + "/" + im
        img = cv2.imread(img)
        
        height, width, channels = img.shape
        print (height, width, channels)


        title = img[0:500, 0:width]
        save_file(cropped,title)

        rate = height//5

        menu = img[height-rate:height, 0:width]
        save_file(cropped,menu)

        if folder == input_line:
            
            line3 = img[(3*height)//7:(4*height)//7, 0: width]
            save_file(cropped,line3)
            
            line4 = img[(4*height)//7:(5*height)//7, 0: width]
            save_file(cropped,line4)

            line5 = img[(5*height)//7:(6*height)//7 , 0: width]
            save_file(cropped,line5)

            line6 = img[(6*height)//7:height , 0: width]
            save_file(cropped,line6)

        if folder  == input_divide_screen:

            content = img[rate:height -rate , 0:width]

            haft = 2* width//5

            haft_content_left = img[rate : height - rate, 0 : haft ]
            save_file(cropped,haft_content_left)

            haft_content_right = img[rate:height - rate, haft : width ]
            save_file(cropped,haft_content_right)

        if folder == input_popup:

            popup = img[height//5:(4*height)//5 , width//6: (5*width)//6]
            save_file(cropped,popup)
            
            popup_title = img[450: 770 , width//6: (5*width)//6]
            save_file(cropped,popup_title)

            popup_content = img[770:1560 , width//6: (5*width)//6]
            save_file(cropped,popup_content)

            popup_button = img[1560:1990 , width//6: (5*width)//6]
            save_file(cropped,popup_button)



        



