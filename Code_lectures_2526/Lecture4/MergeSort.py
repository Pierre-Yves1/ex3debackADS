def mergeSort(list):
    if len(list) > 1:
        # Merge sort the first half
        firstHalf = list[ : len(list) // 2] #lijst in 2 delen
        mergeSort(firstHalf) #mergesort toep op 1e deel

        # Merge sort the second half
        secondHalf = list[len(list) // 2 : ]
        mergeSort(secondHalf) #mergesort toep op 2de deel

        # Merge firstHalf with secondHalf into list
        merge(firstHalf, secondHalf, list) #nadien die 2 die gesorteerd zijn gaan mergen
        #zorgen dat je ze op juiste plaats merged
# Merge two sorted lists */
def merge(list1, list2, temp):
    current1 = 0  # Current index in list1
    current2 = 0  # Current index in list2
    current3 = 0  # Current index in temp

    while current1 < len(list1) and current2 < len(list2): #zolang er elementen zijn in beide lijsten zit je in dit verhaal
        if list1[current1] < list2[current2]:
            temp[current3] = list1[current1] #elemet uit list1 toevoegen aan nieuwe lijst temp
            current1 += 1
            current3 += 1
        else:
            temp[current3] = list2[current2]
            current2 += 1
            current3 += 1

    while current1 < len(list1): #deze komende 2 wile zijn voor als ene list langer is dan andere
        temp[current3] = list1[current1]
        current1 += 1
        current3 += 1

    while current2 < len(list2):
        temp[current3] = list2[current2]
        current2 += 1
        current3 += 1

def main():
    list = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
    mergeSort(list)
    for v in list:
        print(v, end = " ")

main()

# ------------------
# code van in dodona:
# def mergesort(list):
#     if len(list) > 1:
#         # Merge sort the first half
#         firstHalf = list[ : len(list) // 2] #lijst in 2 delen
#         mergesort(firstHalf) #mergesort toep op 1e deel
#
#         # Merge sort the second half
#         secondHalf = list[len(list) // 2 : ]
#         mergesort(secondHalf) #mergesort toep op 2de deel
#
#         # Merge firstHalf with secondHalf into list
#         merge(firstHalf, secondHalf, list) #nadien die 2 die gesorteerd zijn gaan mergen
#         #zorgen dat je ze op juiste plaats merged
#     return list #DIT MOEST ER NOG BIJ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# # Merge two sorted lists */
# def merge(list1, list2, temp):
#     current1 = 0  # Current index in list1
#     current2 = 0  # Current index in list2
#     current3 = 0  # Current index in temp
#
#     while current1 < len(list1) and current2 < len(list2): #zolang er elementen zijn in beide lijsten zit je in dit verhaal
#         if list1[current1] < list2[current2]:
#             temp[current3] = list1[current1] #elemet uit list1 toevoegen aan nieuwe lijst temp
#             current1 += 1
#             current3 += 1
#         else:
#             temp[current3] = list2[current2]
#             current2 += 1
#             current3 += 1
#
#     while current1 < len(list1): #deze komende 2 wile zijn voor als ene list langer is dan andere
#         temp[current3] = list1[current1]
#         current1 += 1
#         current3 += 1
#
#     while current2 < len(list2):
#         temp[current3] = list2[current2]
#         current2 += 1
#         current3 += 1

 
