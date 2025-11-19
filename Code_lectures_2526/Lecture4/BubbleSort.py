def bubbleSort(lst):
    needNextPass = True
    
    k = 1
    while k < len(lst) and needNextPass:
        # List may be sorted and next pass not needed
        needNextPass = False #je zet hem eerst op false maar vanaf je een swap doet (zie onderstaande code), eronder zet je hem opnieuw op true
        for i in range(len(lst) - k): #loopt tot lengte - k dus altijd minder, - k want op einde lijst staan die al goed
            if lst[i] > lst[i + 1]:
                # swap lst[i] with lst[i + 1]
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
          
                needNextPass = True # Next pass still needed #vanaf dat je een swap doet, zet je hem op true. Want als je geen swap meer gedaan hebt weet je dat de lijst gesorteerd is en hoef je dus niet meer verder te gaan, dus dit is stopconditie

def main():
    lst = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
    bubbleSort(lst)
    for v in lst:
        print(v, end = " ")

main()
