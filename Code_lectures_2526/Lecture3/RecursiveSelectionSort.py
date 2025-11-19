#Recursive selection sort zoekt telkens het kleinste element in het deel lst[low..high], zet dat vooraan, en roept zichzelf opnieuw op voor low+1.
# De recursie stopt wanneer low >= high.

def sort(lst):
    sortHelper(lst, 0, len(lst) - 1) # Sort the entire lst

def sortHelper(lst, low, high):
    if low < high:
        # Find the smallest number and its index in lst[low .. high]
        indexOfMin = low;
        min = lst[low];
        for i in range(low + 1, high + 1):
            if lst[i] < min:
                min = lst[i]
                indexOfMin = i

        # Swap the smallest in lst[low .. high] with lst[low]
        lst[indexOfMin] = lst[low]
        lst[low] = min

        # Sort the remaining lst[low+1 .. high]
        sortHelper(lst, low + 1, high) #low+ 1 en high blijft zelfde, dit is recursieve oproep

def main():
    lst = [3, 2, 1, 5, 9, 0]
    sort(lst)
    print(lst)

main()
