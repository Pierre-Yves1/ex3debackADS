## Dit programma telt hoe vaak elk woord voorkomt in een tekstbestand en toont:
# de woorden
#
# samen met hun aantal
#
# gesorteerd volgens aantal (van veel → weinig)

def main():
    # Prompt the user to enter a file
    filename = input("Enter a filename: ").strip()
    inputFile = open(filename, "r") # Open the file

    wordCounts = {} # Create an empty dictionary to count words #lege dictionary aanmaken
    for line in inputFile:
        processLine(line.lower(), wordCounts)
    inputFile.close() 
    
    pairs = list(wordCounts.items()) # Get pairs from the dictionary #key met value erbij

    items = [[x, y] for (y, x) in pairs] # Reverse pairs in the list # Omdat we willen sorteren op het aantal → dus het getal moet op positie 0 staan.

    items.sort() # Sort pairs in items # Standaard sorteert Python lijsten van laag naar hoog op het eerste element.

    for i in range(len(items) - 1, 0, -1): ## Printen in omgekeerde volgorde, We lopen van laatste index naar eerste om
        ##print woorden van meest → minst voorkomend
        print(items[i][1] + "\t" + str(items[i][0]))  ## die eerste [] wil zeggen eerste rij en tweede [] wil zeggen: vb [1]: 2de element v eerste rij
  
# Count each word in the line
def processLine(line, wordCounts): 
    line = replacePunctuations(line) # Replace punctuations with space
    words = line.split() # Get words from each line
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1 #als woord al in dictionary zit, dan teller +1
        else:
            wordCounts[word] = 1 #woord toevoegen a dictionary en teller op 1 zetten

# Replace punctuations in the line with space
def replacePunctuations(line): # als er speciaal teken in voorkomt, verander dat naar een spatie
    for ch in line:
        if ch in '~@#$%^&*()_-+=~"<>?/,.;!{}[]|':
            line = line.replace(ch, " ")

    return line

main()
