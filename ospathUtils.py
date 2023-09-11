import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    # print (os.name)

# check for item existence, if it is file or directory - using the path functions (return booleans)
    # print ("Item exist: ", path.exists("textfile.txt"))

    # print("Item is file: " , path.isfile("textfile.txt"))

    # print("Item is a directory: ", path.isdir("textfile.txt"))

#Work with the file paths
# print ("Item's path: ", path.realpath("textfile.txt"))
# print ("Item's path and name: ", path.split(path.realpath("textfile.txt")))

#Get the modification time
#path.getmtime("textfile.txt") is a time object.  The timestamp
    # print (path.getmtime("textfile.txt"))
    t = time.ctime(path.getmtime("textfile.txt")) # this put it in human readable time
    print (t)
    print (datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))) #other version using datetime function
    
#Calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print ("It has been: ", td , " since the file has been modified")
    print ("Or , ", td.total_seconds() , " Seconds")









if __name__ == "__main__":
    main()
