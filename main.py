import os
import shutil
import pathlib
import Validate
from folders import * 

#Tasks:
'''
1- fix the validation done
'''
class Main(Main_Folders):

    print("current files in folder: ")
    folder_length= len(os.listdir(Main_Folders.main_folder))
    list= os.listdir(Main_Folders.main_folder)

    if folder_length > 0:
        counter = 1

        for file in list:

            print("file No[",counter,"]: ",file)

            file_name , extension = os.path.splitext(file)
            #print(file_name + " => " + extension + "\n") #split the file name and the extension..
            counter+=1
        
            # IMAGES
            if (extension == ".jpg"):
                print("file type: Image." )
                print("Extension: " + extension + "\n")

                script_path = os.path.join(Main_Folders.main_folder , file) #got the script full path #/home/milad/Desktop/filetest/unnamed.jpg
                Validate.Validation.check_folders("image")
                shutil.move(script_path, Main_Folders.image_folder) #move the script to image folder
                Validate.Validation.validate_transfer("images",file) #file : unnamed.jpg


            # DOCUMENTS
            elif (extension == ".pdf"):
                print("file type: PDF." )
                print("Extension: " + extension +"\n")

                script_path = os.path.join(Main_Folders.main_folder,file) #getting the full path of the file to this variable
                Validate.Validation.check_folders("document")
                shutil.move(script_path, Main_Folders.documents_folder)   #move the script to the new existing folder
                Validate.Validation.validate_transfer("pdfs",file) #file : unnamed.jpg


            # TEXTS
            elif (extension == ".txt"):
                print("file type: TEXT." )
                print("Extension: " + extension +"\n")

                script_path = os.path.join(Main_Folders.main_folder,file) #getting the full path of the file to this variable
                Validate.Validation.check_folders("text")
                shutil.move(script_path, Main_Folders.text_folder)   #move the script to the new existing folder
                Validate.Validation.validate_transfer("texts",file) #file : unnamed.jpg

            #on hold...
            elif (extension == ""):
                continue


    else:
        print("no files were found in main folder.")