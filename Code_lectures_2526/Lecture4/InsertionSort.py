# The function for sorting elements in ascending order
def insertionSort(lst):
    # We beginnen vanaf index 1, want index 0 is vanzelf 'gesorteerd'
    for i in range(1, len(lst)):
        # currentElement is het element dat we willen invoegen
        currentElement = lst[i]

        # k is de index van het vorige element (in het al-gesorteerde deel)
        k = i - 1

        # Terwijl k niet buiten de lijst valt EN
        # terwijl het element links groter is dan currentElement:
        # schuif het linkse element één plaats naar rechts
        #
        # Dit maakt plaats om currentElement op de juiste positie te zetten
        while k >= 0 and lst[k] > currentElement:
            lst[k + 1] = lst[k]   # schuif element naar rechts
            k -= 1                # ga verder naar links

        # Hier stopt de while-lus.
        # k staat nu op de positie waarbij:
        # lst[k] <= currentElement   OF   k = -1
        #
        # Daarom moet currentElement in lst[k + 1] komen.
        lst[k + 1] = currentElement


def main():
    lst = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]

    # Sorteer de lijst met insertion sort
    insertionSort(lst)

    # Print de gesorteerde lijst
    for v in lst:
        print(v, end=" ")


main()
