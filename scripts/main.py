import os
import shutil
import pathlib
import Validate
from folders import * 

def folder(user_folder):
        global main_folder
        global image_folder
        global documents_folder
        global text_folder
        main_folder = user_folder  #fields
        image_folder = os.path.join(main_folder,"imagetest")     #"/home/milad/Desktop/filetest/imagetest"
        documents_folder = os.path.join(main_folder,"documentstest")                            #"/home/milad/Desktop/filetest/documentstest"
        text_folder = os.path.join(main_folder,"texttest")     #"/home/milad/Desktop/filetest/texttest"

class Main():

    def run_organizer():
        print(documents_folder)

        print("current files in folder: ")
        folder_length= len(os.listdir(main_folder))
        list= os.listdir(main_folder)

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

                    script_path = os.path.join(main_folder , file) #got the script full path #/home/milad/Desktop/filetest/unnamed.jpg
                    Validate.Validation.check_folders("image",image_folder)
                    shutil.move(script_path, image_folder) #move the script to image folder
                    Validate.Validation.validate_transfer("images",file , image_folder) #file : unnamed.jpg


                # DOCUMENTS
                elif (extension == ".pdf"):
                    print("file type: PDF." )
                    print("Extension: " + extension +"\n")

                    script_path = os.path.join(main_folder,file) #getting the full path of the file to this variable
                    Validate.Validation.check_folders("document",documents_folder)
                    shutil.move(script_path, documents_folder)   #move the script to the new existing folder
                    Validate.Validation.validate_transfer("pdfs",file , documents_folder) #file : unnamed.jpg


                # TEXTS
                elif (extension == ".txt"):
                    print("file type: TEXT." )
                    print("Extension: " + extension +"\n")

                    script_path = os.path.join(main_folder,file) #getting the full path of the file to this variable
                    Validate.Validation.check_folders("text",text_folder)
                    shutil.move(script_path, text_folder)   #move the script to the new existing folder
                    Validate.Validation.validate_transfer("texts",file , text_folder) #file : unnamed.jpg

                #on hold...
                elif (extension == ""):
                    continue

        else:
            print("no files were found in main folder.")

#main=Main()
#main.run_organizer()