"""This is my practice file for the os module"""

import os
import os.path

# LISTING FILES IN A DIRECTORY/FOLDER
# os.listdir() function returns a list of contents in the dir given by path.

for filename in os.listdir('.'):
    print(filename)

# CREATE A DIR
# os.mkdir() function creates a directory.
# os.mkdir('new_directory')

# CHANGE YOUR WORKING DIR
os.chdir('/Users/ecemkaraman/Desktop/cyber')

# GET YOUR CURRENT WORKING DIR
current_directory = os.getcwd()
print(current_directory)

current_dir = os.getcwd()
file_name = "sample1.txt"
file_path = current_dir + "/" + file_name

# RENAME A FILE OR DIR
os.rename('old_filename', 'new_filename')

# DELETE A FILE - It cant delete directories
os.remove('filename')

# EXECUTING A SHELL COMMAND
os.system('ls -l')

import os

# Need to use to print the outcome in most
# os.name: Return info about what platform you are running on
# ‘posix’ - MacOS,Linux
# ‘nt’- Windows
print(os.name)

# os.environ: Return a dict of the user's environmental variables
# e.g. path, number of processors, type of CPU, computer name...
os.environ

#We can use dict methods with os.environ
#KeyError if the key doesn't exist
print(os.environ["PATH"])

# os.getenv() is better to access the env variable
# If the key doesn't exist, it returns None
print(os.getenv("PATH"))

# os.getcwd() Get current working directory
print(os.getcwd())

# os.chdir : Change working dir
os.chdir("./linux")

# os.mkdir(): Create a single folder
# os.mkdir("test")
print(os.listdir())

# os.makedirs(): Create all intermediate folders in a path if they don't exist
# You can create a path with nested folders inside
path="/Users/ecemkaraman/PycharmProjects/linux/folder1/folder2/folder3"
os.makedirs(path)
print(os.listdir())
# os.remove(): Delete files
# os.unlink does the same thing - for Unix

# os.rmdir(): Delete directories - only for empty dirs
# delete all the files first via remove()
os.rmdir("test")

# Remove nested empty directories recursively
# Starts from the leaf and recurses to the parent
# OSError if any dir isn't empty or locked/inaccessible
os.removedirs("folder1/folder2/folder3")

file_path = 'myfile.txt'

with open(file_path, 'w'):
    pass
# Rename a file or folder (oldname, newname)
os.rename('myfile.txt', 'empty_file2.txt')

# Recursively renames a directory/file
# Syntax: os.renames(old_path, new_path)
# If the dest directory doesn't exist, it'll be created
os.renames('folder1/folder2/folder3', 'foldera/folderb/folderc')

# Iterate over a root level path - traverse directory
# Pass it a path & get access to all its subdirectories&files
mypath=r'/Users/ecemkaraman/PycharmProjects'
for root, dirs, files in os.walk(mypath):
    print(root)
    for _dir in dirs:
        print(_dir)
    for _file in files:
        print(_file)

# os.path is a submodule with some functions inside
# basename, dirname, exists, isdir, isfile, join, split
# os.path.basename() - return the filename portion of a path
os.path.basename('/Users/ecemkaraman/PycharmProjects/linux/empty_file2.txt')

# Return just the directory portion of path
os.path.dirname('/Users/ecemkaraman/PycharmProjects/linux/empty_file2.txt')

# If you pass a directory that ends in a folder instead of a file, it returns up to the parent but not cwd
os.path.dirname(os.getcwd())

# Bool - does the path exist?
os.path.exists('/Users/ecemkaraman/PycharmProjects/linux/empty_file1.txt')

# Bool - checks if the path is a directory/file
os.path.isdir('/Users/ecemkaraman/PycharmProjects/linux/empty_file1.txt')
os.path.isfile('/Users/ecemkaraman/PycharmProjects/linux/empty_file2.txt')

# Join comma-separated paths together with the relevant separator
#  Use \ for Windows and / for Linux
# It doesn't check if the result actually exists
os.path.join(r'/Users/ecemkaraman', 'PycharmProjects/linux/empty_file2.txt')

# Split a path into a tuple (dir + file)
os.path.split(r'/Users/ecemkaraman/PycharmProjects/linux/empty_file2.txt')
# If there is no file in the path, the last subfolder becomes the 2nd tuple element
# Generally if there's no file in the path, the last subfolder is treated like the file
os.path.split(r'/Users/ecemkaraman/PycharmProjects/linux')
# Multi-assignment from the tuple
dirname, filename = os.path.split(r'/Users/ecemkaraman/PycharmProjects/linux/empty_file2.txt')
print(dirname)
print(filename)



# HOW TO RECURSE/TRAVERSE A DIRECTORY
# Method1: os.walk()
# Works for both Linux&Mac - similar filesystem APIs
def traverse_directory(path):
    for root, dirs, files in os.walk(path):
        # 'root' is the current directory being traversed
        # 'dirs' is a list of subdirectories in 'root'
        # 'files' is a list of files in 'root'
        for file_name in files:
            full_path = os.path.join(root, file_name)
            # Process each file using 'full_path'

# Example usage:
traverse_directory('/path/to/directory')

# Method2: pathlib -->path.iterdir()
from pathlib_pr import Path

def traverse_directory1(path):
    path1 = Path(path)
    for item in path.iterdir():
        if item.is_dir():
            traverse_directory(item)  # Recursive call for subdirectories
        else:
            # Process each file using 'item'