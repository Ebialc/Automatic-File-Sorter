import os

import shutil


# Change to your downloads folder

downloads_folder = 'D:\Downloads'


# Set the categories for organizing files

categories = {

    'images': ['jpg', 'jpeg', 'png', 'gif', 'bmp'],

    'videos': ['mp4', 'avi', 'mov', 'wmv'],

    'executables': ['exe'],

    'documents': ['docx', 'doc', 'pdf', 'txt', 'epub', 'pptx', 'ppt', 'xlsx'],

    'audio': ['mp3', 'wav', 'ogg'],

    'archives': ['zip', 'rar', '7z', 'tar' ,'pkg'],

    'others': []  # catch-all for unknown file types

}


# Create the category folders if they don't exist

for category in categories:

    category_folder = os.path.join(downloads_folder, category)

    if not os.path.exists(category_folder):

        os.makedirs(category_folder)


# Iterate through the files in the downloads folder

for filename in os.listdir(downloads_folder):

    filepath = os.path.join(downloads_folder, filename)

    if os.path.isfile(filepath):

        # Get the file extension

        file_ext = os.path.splitext(filename)[1][1:].lower()


        # Determine the category for the file

        for category, extensions in categories.items():

            if file_ext in extensions:

                category_folder = os.path.join(downloads_folder, category)

                shutil.move(filepath, category_folder)

                break

        else:

            # If the file type is unknown, move it to the 'others' folder

            others_folder = os.path.join(downloads_folder, 'others')

            shutil.move(filepath, others_folder)


print("Downloads folder organized!")