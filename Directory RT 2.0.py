import os
space = ""
print(space)
Directory = os.getcwd()
FilesInDirectory = os.listdir(Directory)
PythonFile = os.path.basename(__file__)
FilesInDirectory.remove(PythonFile)
print(FilesInDirectory)
print(space)
FileName = str(input("Name for the files? "))
x = input("What # do you want to start from? ")
for file in FilesInDirectory:
    FileExtension = os.path.splitext(file)
    FileExtension = FileExtension[1]
    print(FileExtension)
    x = str(x)
    print(Directory + file)
    os.rename(Directory + '\\' + file, Directory + "\\" + FileName + " " + x + FileExtension)
    x = int(x)
    x +=1
    print (file)

