class Stack:
    def __init__(self):
        self.__elements = []
# Die __ vóór “elements” in begin vd code zorgt ervoor dat we een private lijst maken, dwz dat je altijd moet werken met die gedefinieerde methodes, je kan dus niet het eerste element eraf halen, zo forceer je die stack aanpak!
# Dus eerst maak je een lijst aan maar door die methodes eraan te koppelen forceer je het eigenlijk naar een stack!
# Je hebt dus een datastructuur gemaakt die enkel deze methodes toelaat
# Lijst dus zien als soort v onderliggende structuur voor uw stack

    # Er wordt lijst ‘elements’ aangemaakt(stack)(stack w geimplementeerd adhv een
    # lijst) (lijst heeft naam in mijn classe, nl.‘elements’).Daaraan verschillende operaties
    # aan koppen, vb is mijn stack leeg? Ja als lengte lijst = 0

# Dit zijn de enigste methodes die je mag gebruiken om aan de lijst te komen

    # Return true if the stack is empty
    def isEmpty(self):
        return len(self.__elements) == 0
    
    # Returns the element at the top of the stack 
    # without removing it from the stack.
    def peek(self): #Peek is andere methode/operatie die bij de stack hoort: kijken wat er bovenaan staat, zonder het eraf te halen! Je retourneert wat er op einde v lijst staat
        if self.isEmpty():
            return None
        else:
            return self.__elements[len(self.__elements) - 1]

    # Stores an element into the top of the stack
    def push(self, value): #Push is element eraan toevoegen, in lijst is dat gwn ‘append”
        self.__elements.append(value)

    # Removes the element at the top of the stack and returns it
    def pop(self): #Pop is bovenste element er vanaf gaan halen (pop is functie binnen lijst in python)
        if self.isEmpty():
            return None
        else:
            return self.__elements.pop() 
    
    # Return the size of the stack
    def getSize(self):
        return len(self.__elements)