def main():
    # Open file for input
    inputFile = open("Presidents.txt", "r")
    print("(1) Using read(): ")
    print(inputFile.read()) # Read all in the file
    inputFile.close() # Close the input file

    # Open file for input
    inputFile = open("Presidents.txt", "r")
    print("\n(2) Using read(number): ") #\n wil zeggen begin op volgende lijn
    s1 = inputFile.read(5)  #5: lees eerste 5letters
    print(s1)
    s2 = inputFile.read(15) # Read 15 characters to s2   #15: lees volgende 15 letters
    print(repr(s2)) #repr() toont de string zonder iets te verbergen, zien exact welke 15 karakters zijn ingelezen, ziet of er \n, spaties, of andere verborgen karakters** zitten

    inputFile.close() # Close the input file

    # Open file for input
    inputFile = open("Presidents.txt", "r")
    print("\n(3) Using readline(): ")
    line1 = inputFile.readline() # Read a line
    line2 = inputFile.readline() #leest lijn per lijn
    line3 = inputFile.readline()
    line4 = inputFile.readline()
    print(repr(line1))
    print(repr(line2))
    print(repr(line3))
    print(repr(line4))
    inputFile.close() # Close the input file

    # Open file for input
    inputFile = open("Presidents.txt", "r")
    print("\n(4) Using readlines(): ") #leest alles in 1 keer in
    print(inputFile.readlines())
    inputFile.close() # Close the input file
# ➡️ Leest de volledige file
#    ➡️ Geeft een lijst terug
#    ➡️ Elke lijn in het bestand wordt één element in de lijst
main() # Call the main function
