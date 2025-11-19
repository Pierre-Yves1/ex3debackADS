import os
# import os haalt de bibliotheek binnen die leidt de code in staat stelt om te werken met bestanden, directories, paden en bestandsinformatie.
# Zonder import os zou je code een fout geven omdat Python anders niet weet wat os, os.path.isfile, os.listdir, etc. zijn.

def main():
    # Prompt the user to enter a directory or a file
    path = input("Enter a directory or a file: ").strip()   
   
    # Display the size
    try:
        print(getSize(path), "bytes")
    except:
        print("Directory or file does not exist")

def getSize(path):
    size = 0 # Store the total size of all files

    if not os.path.isfile(path): #als het geen file is, is het een directory, dan haal je alle files en/of directories daaronder op
        lst = os.listdir(path) # All files and subdirectories
        for subdirectory in lst:
            size += getSize(path + "\\" + subdirectory) 
    else: # Base case, it is a file #het is wel een file, dan kan je gwn direct beginnen tellen
        size += os.path.getsize(path) # Accumulate file size 

    return size

main() # Call the main function
