#%%

import os

folders=os.listdir("images for OS module pratice")#this makes the list of all the files in the folder
print(folders)

for i in range(0,len(folders)):#using for loop to rename all the files in the folder
    if(folders[i].endswith(".jpg")):
        os.rename(f"images for OS module pratice/{folders[i]}",f"images for OS module pratice/image{(i+1)}.jpg")

foldersnew=os.listdir("images for OS module pratice")
print(foldersnew)


