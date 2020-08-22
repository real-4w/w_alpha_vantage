# cleanup all *png files in the directory
import os 
import pathlib
from os import listdir
folder_path = pathlib.Path.cwd()
for file_name in listdir(folder_path):
    if file_name.endswith('.png'):
        os.remove(file_name)