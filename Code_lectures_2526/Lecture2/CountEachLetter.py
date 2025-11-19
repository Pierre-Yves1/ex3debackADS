## telt hoe vaak elke letter (a–z) voorkomt
# telt letters met ASCII-truc (ord() / chr())
def main():
    filename = input("Enter a filename: ").strip() #strip om alle spaties weg te doen zodat er geen problemen zijn met het openen vd file
    inputFile = open(filename, "r") # Open the file

    counts = 26 * [0] # Create and initialize counts # lijst creeren met 26 plaatsne die op 0 staan nu
    # Één plaats per letter in het alfabet.
    for line in inputFile:
        # Invoke the countLetters function to count each letter
        countLetters(line.lower(), counts)#zet de tekst naar kleine letters om (geen verschil tussen A en a)
    
    # Display results
    for i in range(len(counts)):
        if counts[i] != 0:
            print(chr(ord('a') + i) + " appears " + str(counts[i])
              + (" time" if counts[i] == 1 else " times"))

    inputFile.close() # Close file
  
# Count each letter in the string 
def countLetters(line, counts): 
    for ch in line:
        if ch.isalpha(): # Test if ch is a letter
            counts[ord(ch) - ord('a')] += 1
            # ord(ch) - ord('a') berekent de index:
            #
            # Voorbeeld: ch = 'd'
            #
            # ord('d') = 100
            #
            # ord('a') = 97
            #
            # 100 − 97 = 3 → index 3 is de 4de letter

main() # Call the main function
