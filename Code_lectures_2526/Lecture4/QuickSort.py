def quickSort(lst):  #das deze oef waar gailly extra kort filmpje over maakte met die pivot
    quickSortHelper(lst, 0, len(lst) - 1)

def quickSortHelper(lst, first, last):
    if last > first: # Als het deel minstens 2 elementen bevat → sorteer verder.

        pivotIndex = partition(lst, first, last)
        quickSortHelper(lst, first, pivotIndex - 1) #Sorteer het linker stuk van de lijst (alles kleiner dan pivot)
        quickSortHelper(lst, pivotIndex + 1, last) #Sorteer het rechter stuk van de lijst (alles groter dan pivot)

# Partition lst[first..last] 
def partition(lst, first, last): # pivot kiezen, verkeerd geplaatste elementen wisselen, pivot op juiste positie zetten
    pivot = lst[first]  # Choose the first element as the pivot
    low = first + 1  # Index for forward search
    high = last  # Index for backward search

    while high > low:
        # Search forward from left
        while low <= high and lst[low] <= pivot:
            low += 1

        # Search backward from right
        while low <= high and lst[high] > pivot:
            high -= 1

        # Swap two elements in the list
        if high > low:
            lst[high], lst[low] = lst[low], lst[high]

    while high > first and lst[high] >= pivot:
        high -= 1

    # Swap pivot with lst[high]
    if pivot > lst[high]:
        lst[first] = lst[high]
        lst[high] = pivot
        return high
    else:
        return first
