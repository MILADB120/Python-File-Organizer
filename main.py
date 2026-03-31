import os
import shutil
import pathlib

#Tasks:
'''
1- finish the full file path. done
2- move the file to another folder. done
3- move the file to another folder after creating a new folder.
4- make a folder for .text then check if it exists then move the .text file to the new folder(directory)

'''
#where files live.
main_folder = "/home/milad/Desktop/filetest" 
image_folder = "/home/milad/Desktop/testimage"
documents_folder = "/home/milad/Desktop/documentstest"

#sort files
images=[]
pdfs=[]

files_in_folder = os.listdir("/home/milad/Desktop/filetest")

if len(files_in_folder) > 0:
    counter = 1

    for file in files_in_folder:
        print("file No[",counter,"]: ",file)

        file_name , extension = os.path.splitext(file)
        print(file_name + " => " + extension + "\n") #split the file name and the extension..
    
        if (extension == ".jpg"):
            images.append(file)
            script_path = os.path.join(main_folder , file) 
            #print(script_path) all good

            shutil.move(script_path, image_folder)
            print("The file has been moved to testimage folder \n")

        elif (extension == ".pdf"):
            pdfs.append(file)

            script_path = os.path.join(main_folder,file)
            shutil.move(script_path, documents_folder)
            print("The file has been moved to documentsfolder folder \n")

        #on hold...
        elif (extension == ""):
            continue

        counter+=1

else:
    print("no files were found in main folder.")


for item in images:
    print("all images in the folder: " , item)

for item in pdfs:
    print("all pdf in the folder: " ,item)
