import os
space = ""
print(space)
Directory = os.getcwd()
FilesInDirectory = os.listdir(Directory)
ExtensionLibrary = [] 

#below removes python file from the array of files in current directory.
PythonFile = os.path.basename(__file__)
FilesInDirectory.remove(PythonFile)

print(FilesInDirectory)
print(space)


negativeResponses = ['No', 'N', 'n', 'NO ', 'N ', 'n ', 'no ', 'No ', 'no', 'NO']
positiveResponses = ['Yes','Y','n','YES ','Y ','y ','yes ','Yes ', 'yes', 'YES']

ErrorRepeater = 1

while (ErrorRepeater == 1):
    ErrorRepeater = 0
    Q1 = input("Basic naming? [y/n] ")
    if (Q1 in negativeResponses):
        #quickly scans files and returns the file extensions.
        for file in FilesInDirectory:
            FileExtension = os.path.splitext(file)
            FileExtension = FileExtension[1]
            ExtensionLibrary.append(FileExtension)

        #removes duplicates    
        ExtensionLibrary = list(set(ExtensionLibrary))

        #returns a # of current extensions in the directory.
        NumOfExtensions = str(len(ExtensionLibrary))
        print(space)
        print(ExtensionLibrary)
        print(space)
        print("# of Extensions: " + NumOfExtensions)
        print(space)
            
        #Advanced renaming process
        for Extension in ExtensionLibrary:
            FileName = str(input("Name for the " + Extension + " files? "))
            x = input("What # do you want to start from for the " + Extension + " type? ")
            if (x == "" or x == " "):
                x = 1  
            for file in FilesInDirectory:
                FileExtension = os.path.splitext(file)
                FileExtension = FileExtension[1]
                try:
                    x = int(x)
                    x = str(x)
                    if (FileExtension == Extension):
                        os.rename(Directory + '\\' + file, Directory + "\\" + FileName + x + FileExtension)
                        print (FileName + x + FileExtension)
                        x = int(x)
                        x +=1
                        x = str(x)
                        
                except:
                    print(space)
                    print("Invalid input, put in #'s not letters.")
                    ErrorRepeater = 1
                    print(space)
                    break
    elif (Q1 in positiveResponses):
        print(space)
        FileName = str(input("Common name for all files? "))
        print(space)
        x = input("What # do you want to start from? ")
        print(space)
        if (x == "" or x == " "):
            x = 1
        for file in FilesInDirectory:
            FileExtension = os.path.splitext(file)
            FileExtension = FileExtension[1]
            ExtensionLibrary.append(FileExtension)
            try:
                x = int(x)            
                x = str(x)
                print(file)
                print (FileName + " " + x + FileExtension)
                os.rename(Directory + '\\' + file, Directory + "\\" + FileName + " " + x + FileExtension)
                x = int(x)
                x +=1
            except:
                print(space)
                print("Invalid input, put in #'s not letters.")
                ErrorRepeater = 1
                print(space)
                break

    else:
        print(space)
        print ("Invalid input, answer with either y/n")
        ErrorRepeater = 1
        print(space)
