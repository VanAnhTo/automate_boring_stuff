import cv2
import os
import datetime


def new_file_name():
    now = datetime.datetime.now()
    new_file_name = now.strftime("%Y%m%d_%H%M%S%f"+ ".png")
    return new_file_name

def save_file(path,name):
    new_file = path + new_file_name()
    cv2.imwrite(new_file, name)
    return
