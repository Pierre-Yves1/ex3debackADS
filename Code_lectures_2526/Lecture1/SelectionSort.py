# The function for sorting elements in ascending order (Simplified Version)
def selectionSort(lst): #
    for i in range(len(lst) - 1):
        # Find the minimum in the lst[i : len(lst)]
        currentMin = min(lst[i : ]) #Zoekt min in lijst die begin van i en die gaat tot het einde
        currentMinIndex = i + lst[i: ].index(currentMin) #Je telt i eerst erbij, want lijst wordt kleiner en je wilt de positie van in de volledige lijst!
        
        # Swap lst[i] with lst[currentMinIndex] if necessary
        if currentMinIndex != i: #Als beide indeces wel gelijk zijn wil dat zeggen dat kleinste getal al vooraan stond!
            lst[currentMinIndex], lst[i] = lst[i], currentMin
            
def main():
    lst = [-2, 4.5, 5, 1, 2, -3.3]
    selectionSort(lst)
    print(lst)

main()