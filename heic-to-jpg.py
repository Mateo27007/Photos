# -*- coding: utf-8 -*-
"""
HEIC to jpg converter

Created on Sun Jul 23 15:41:22 2023

@author: mateo
"""

from PIL import Image
import os
from os.path import join as osjoin
from os.path import split as ossplit
import glob
from pillow_heif import register_heif_opener

register_heif_opener()


def convert_heic_to_jpg(heic_path, jpg_path):
    heif_file = Image.open(heic_path)
    heif_file.save(jpg_path, format="JPEG")
    folder_path = ossplit(heic_path)[0]
    new_heic = osjoin(folder_path,'heic_files',ossplit(heic_path)[1])
    os.rename(heic_path,new_heic)

def get_folder_choice():
    print("Available folders:")
    folders = [folder for folder in os.listdir() if os.path.isdir(folder)]
    for idx, folder in enumerate(folders, start=1):
        print(f"{idx}. {folder}")
    
    while True:
        try:
            choice = int(input("Enter the number corresponding to the folder: "))
            if 1 <= choice <= len(folders):
                return folders[choice - 1]
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def convert_all_folders_to_jpg():
    chosen_folder = get_folder_choice()
    folder_path = os.path.abspath(chosen_folder)

    for filename in glob.glob(os.path.join(folder_path, "*.HEIC")):
        heic_path = os.path.abspath(filename)
        jpg_path = os.path.splitext(heic_path)[0] + ".jpg"
        heic_folder = osjoin(folder_path,'heic_files')
        if not os.path.exists(heic_folder):
            os.mkdir(heic_folder)

        try:
            convert_heic_to_jpg(heic_path, jpg_path)
            print(f"Converted {filename} to JPG.")
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")

if __name__ == "__main__":
    convert_all_folders_to_jpg()