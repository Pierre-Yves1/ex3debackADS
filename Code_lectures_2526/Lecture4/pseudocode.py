Heel goede vraag — dit is exact wat hij bedoelt met pseudocode geven en jij moet er Python van maken.
De prof gaat géén Python geven, maar taal-neutraal stappenplan zoals:

"herhaal tot lijst gesorteerd is"

"vergelijk opeenvolgende elementen"

"wissel ze indien nodig"

"zoek kleinste in resterende deel"

enz.

Dat is pseudocode.

Hier zijn de soorten pseudocode die de prof typisch kan geven voor bubble sort, selection sort, insertion sort en merge sort. Dit zijn 100% examengerichte voorbeelden.

🟦 1. Mogelijke pseudocode voor Bubble Sort (EXAMENSTIJL)

Deze lijkt bijna zeker examenvraag want hij verwees ernaar in les.

📄 Mogelijke pseudocode:
repeat
    swapped ← false
    for i from 0 to length(A) - 2 do
        if A[i] > A[i+1] then
            swap A[i] and A[i+1]
            swapped ← true
until swapped = false

Wat jij dan moet doen:

👉 Herkennen dat dit bubble sort is
👉 Omzetten naar Python:

def bubble_sort(A):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                swapped = True

🟦 2. Mogelijke pseudocode voor Selection Sort

De prof gaf dit expliciet in de les, dus ook zeer examengericht.

📄 Mogelijke pseudocode:
for i from 0 to n-2 do
    min_index ← i
    for j from i+1 to n-1 do
        if A[j] < A[min_index] then
            min_index ← j
    swap A[i] and A[min_index]

Python:
def selection_sort(A):
    for i in range(len(A) - 1):
        min_index = i
        for j in range(i+1, len(A)):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]

🟦 3. Mogelijke pseudocode voor Insertion Sort

Komt ook vaak in zulke basisreeksen.

📄 Pseudocode:
for i from 1 to n-1 do
    key ← A[i]
    j ← i - 1
    while j ≥ 0 and A[j] > key do
        A[j+1] ← A[j]
        j ← j - 1
    A[j+1] ← key

Python:
def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key

🟦 4. Mogelijke pseudocode voor Merge Sort (recursief)

Omdat het recursie-hoofdstuk samenkomt met sorting — erg examenwaardig.

📄 Examengerichte pseudocode:
function merge_sort(A)
    if length(A) ≤ 1
        return A

    mid ← length(A) / 2
    left ← merge_sort(A[0..mid-1])
    right ← merge_sort(A[mid..end])

    return merge(left, right)


En merge-fase:

function merge(L, R)
    result ← empty list
    while L not empty and R not empty do
        if L[0] ≤ R[0]
            append L[0] to result
            remove L[0]
        else
            append R[0] to result
            remove R[0]
    append remaining elements of L or R
    return result

🟩 5. Wat hij NIET gaat doen

Hij gaat je geen Python geven.
Hij gaat je geen code laten overschrijven.
Hij gaat iets geven zoals:

“Schrijf het algoritme uit in Python dat overeenkomt met volgend pseudocode schema.”

En dan verwacht hij:

herkenning van het algoritme

juiste loops (for/while)

juiste variabelen

correcte Python syntax