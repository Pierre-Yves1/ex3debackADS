from random import randint 

def main():
    # Open file for writing data
    outputFile = open("Numbers.txt", "w")
    for i in range(10):
        outputFile.write(str(randint(0, 9)) + " ") #str gebruiken want textfile verwacht strings ipv numbers + altijd spatie erachter
    outputFile.close() # Close the file

    # Open file for reading data
    inputFile = open("Numbers.txt", "r")
    s = inputFile.read() # Read all data to s
    numbers = [float(x) for x in s.split()] #split zorgt ervoor dat alle elementjes tss de spaties eruit gehaald w
    #float gebruiken om tekst terug in numbers om te zetten zodat je bewerkingen kunt doen
    for number in numbers:
        print(number, end = " ")
    inputFile.close() # Close the file
    
main() # Call the main function
