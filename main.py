import os
import shutil
import pathlib

#Tasks:
'''
1- read files from a folder. #done
2- detect the files type (.pdf .jpg) 
3- sort the files 
'''
#where files live.
folder_path = "/home/milad/Desktop/filetest" 



#read files from a folder 
print("files in folder (filetest) :\n")

files_in_folder = os.listdir("/home/milad/Desktop/filetest")
#print(files_in_folder)
#print(type(files_in_folder)) #list

#sorting..
images=[]
pdfs=[]

counter=1
for file in files_in_folder:

    print("file No[",counter,"]: ",file)

    file_name , extension = os.path.splitext(file)
    print(file_name + " => " + extension + "\n") #split the file name and the extension..
    
    if (extension == ".jpg"):
        images.append(file)
        script_path = os.path.join(folder_path , file)
        print(script_path)
        #shutil.move("/home/milad/Desktop/filetest", "/home/milad/Desktop/testimage")
    
    elif (extension == ".pdf"):
        pdfs.append(file)

    elif (extension == ""):
        continue

    counter+=1

for item in images:
    print("all images in the folder: " , item)

for item in pdfs:
    print("all pdf in the folder: " ,item)
