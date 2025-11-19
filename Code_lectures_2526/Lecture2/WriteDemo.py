def main():
    # Open file for output
    outputFile = open("Presidents.txt", "w")

    # Write data to the file
    outputFile.write("George Washington\n")
    outputFile.write("John Adams\n")
    outputFile.write("Thomas Jefferson") #Write Thomas Jefferson

    outputFile.close() # Close the output file

main() # Call the main function

#🟦 Waarom zetten we dit binnen def main()?
#✅ 1. Om te vermijden dat de code automatisch wordt uitgevoerd bij import
# Stel dat iemand dit bestand importeert:
# import ReadDemo
# Als je geen main() gebruikt, wordt ALLE code die bovenaan staat onmiddellijk uitgevoerd → dus je file wordt geopend, gelezen, geprint… terwijl dat niet de bedoeling is.
# Door het in een functie te steken gebeurt dit alleen wanneer je:
# main()
# roeit.
# Door alles in main() te zetten:
# •	wordt niets uitgevoerd
# •	tot je main() onderaan zet

#------
# 🟩 2. Wat doet with open(...) as f: ?
#
# Voorbeeld:
#
# with open("test.txt", "r") as f:
#     data = f.read()
#     alles erbinnen zetten
#
# ➡️ Python sluit het bestand automatisch, zelfs als:
#
# er een fout gebeurt
#
# je een return uitvoert
#
# de functie stopt
#
# je er niet meer aan denkt
#
# Dit heet een context manager.
#
# Denk aan:
#
# “Open dit
