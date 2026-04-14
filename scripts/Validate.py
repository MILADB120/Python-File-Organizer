import os
from main import *


class Validation():

    def check_folders(script_type,dir_folder):  #check if the folder exists... if not make one
        if script_type == "document" :

            if(not os.path.exists(dir_folder)):
                os.makedirs(dir_folder ,exist_ok=True)
                print("The Documents folder was created.")

            else :
                print("the folder already exists.\nprepering for moving..")
        
        elif script_type == "image" :
             
            if(not os.path.exists(dir_folder)):
                os.makedirs(dir_folder ,exist_ok=True)
                print("The Images folder was created.")

            else :
                print("the folder already exists.\nprepering for moving..")


        elif script_type == "text" :

            if(not os.path.exists(dir_folder)):
                os.makedirs(dir_folder ,exist_ok=True)
                print("The Images folder was created.")

            else :
                print("the folder already exists.\nprepering for moving..")

            

    def validate_transfer(folder, file_name, check): #testing for images

        if folder == "images":

            new_path = os.path.join(check,file_name  ) #get the new path were the image should be now

            if os.path.exists(new_path) :
                print("the script has been moved successfully.\n")
        
            else :
                print("Error.")
        
        if folder == "pdfs":

            new_path = os.path.join(check,file_name  ) #get the new path were the image should be now

            if os.path.exists(new_path) :
                print("the script has been moved successfully.\n")
        
            else :
                print("Error.")

        if folder == "texts":

            new_path = os.path.join(check,file_name  ) #get the new path were the image should be now

            if os.path.exists(new_path) :
                print("the script has been moved successfully.\n")
        
            else :
                print("Error.")
            
