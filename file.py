import os
import shutil
import datetime

now = datetime.datetime.now()

#filename = "foo/bar/baz.txt"
folder_name = "backup"
file_name = "download.png"
os.makedirs(folder_name, exist_ok=True)
new_file_name = now.strftime("%Y%m%d%H%M%S.png")
shutil.move( file_name, folder_name + "/" + new_file_name)

print (now.strftime("%Y%m%d%H%M%S") + '.png')

