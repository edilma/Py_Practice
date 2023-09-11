import os
from os import path
import shutil


def main():
    #create a file and directory
    directory = "results"
    file = open("results.txt", "w+")
    # Get current directory
    currentDirectory = os.getcwd()

    # create a folder
    newPath = os.path.join(currentDirectory,directory)
    os.makedirs(newPath)

    # make a list of the file names(string) 
    listFiles = os.listdir(currentDirectory) 
    totalBytes = 0
    for f in listFiles:
        totalBytes = totalBytes + os.path.getsize(f)
        file.write(f + "\n")
    
    #write the total byte count
    tbytes = str(totalBytes)
    file.write("Total number of bytes: " + tbytes)
    file.close()

    #move the file inside the results directory
    destinationPath = os.path.join(newPath,"results.txt" )
    sourcePath = os.path.join(currentDirectory,"results.txt")
    
    shutil.move(sourcePath, destinationPath)



if __name__ == "__main__":
    main()