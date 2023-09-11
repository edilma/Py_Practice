'''
How to create a new directory.  
In this case, it is created inside the current directory
'''

import os

def main():
    newDirectory = "NewDirectory"
    currentDirectory = os.getcwd()
    #first create the path and then execute the creation
    newPath = os.path.join(currentDirectory,newDirectory)
    os.makedirs(newPath)







if __name__ == "__main__":
    main()