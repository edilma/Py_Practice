import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
     #Duplicate an existing file
    # if path.exists("textfile.txe"):
    #    #Get the path to the file in the current directory (returns a string)
    sourceFile = path.realpath("textfile.txt.bak")
    # #print ("The real path is " , src)
    # destinationFile = sourceFile + ".bak" # this is a variable no a file
    # #print(destinationFile)
    # #create the destination file in the folder 
    # shutil.copy(sourceFile, destinationFile,)

    #rename the original copy
    #os.rename("textfile.txt", "newNameFile.txt")

    #put all items into a ZIP archive
    # root_dir, tail = path.split(sourceFile) # I get a tupple with the root directory and the filename
    #print(root_dir)
    #print (tail)
    # shutil.make_archive("archive","zip", root_dir)  # I zip here everything in the root_dir directory

    # Put specific files in a zip file
    with ZipFile("textzip.zip", "w") as newzip:
        newzip.write("newNameFile.txt")
        newzip.write("textfile.txt.bak")




if __name__ == "__main__":
    main()