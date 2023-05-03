#program to print user's constructed error message#

try:
    fh = open("myfile.txt", "r")
except IOError:
    print("Error: can't find file or read data")
else:
    print("File read successfully")

