# Use binary search to find the key in the list
def binarySearch(lst, key):
    low = 0
    high = len(lst) - 1 # Last index in lst #start te tellen bij 0 dus high = lengte lijst – 1
      
    while high >= low: #Stopconditie? Als de 2 indexen elkaar kruisen, dan ga je get gezochte getal niet meer vinden he!
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return mid
        else:
            low = mid + 1
      
    return -low - 1 # Now high < low, key not found ##Return -1 kan eigenlijk ook gewoon! (dit is gewoon zeggen ‘ik heb het getal niet gevonden’

def main():
    lst = [-3, 1, 2, 4, 9, 23]
    print(binarySearch(lst, 2))
    
main()