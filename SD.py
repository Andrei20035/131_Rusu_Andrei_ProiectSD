def radixSort(arr, base=10):
    if len(arr) == 0:
        return arr
    # determina valoarea maxima din lista
    max_value = max(arr)
    # determina numarul maxim de cifre al valorii maxime
    num_digits = len(str(abs(max_value)))
    # face sortarea dupa cifre, de la cifra cea mai putin semnificativa catre cea mai semnificativa
    for digit in range(num_digits):
        # creeaza "coșuri" goale pentru fiecare cifra (0,1,...,base-1)
        buckets = [[] for _ in range(base)]
        # adauga elementele in coșul corespunzator cifrei curente
        for number in arr:
            # ia cifra curenta
            current_digit = (number // (base ** digit)) % base
            buckets[current_digit].append(number)
        # concateneaza toate coșurile pentru a obține o listă sortată după cifra curentă
        arr = [item for bucket in buckets for item in bucket]
    return arr

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    # imparte lista in doua jumatati
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    # sorteaza fiecare jumatate
    left_half = mergeSort(left_half)
    right_half = mergeSort(right_half)
    # combina cele doua jumatati sortate
    return merge(left_half, right_half)

def merge(left_half, right_half):
    result = []
    i = j = 0
    # combina cele doua jumatati sortate in ordine
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1
    # adauga elementele ramase din jumatatea stanga
    result += left_half[i:]
    # adauga elementele ramase din jumatatea dreapta
    result += right_half[j:]
    return result

def shellSort(arr):
    # determina lungimea listei
    n = len(arr)
    # determina distanta de sortare initiala
    gap = n // 2
    # se executa sortarea cu distante tot mai mici
    while gap > 0:
        for i in range(gap, n):
            current = arr[i]
            j = i
            # muta elementele mai mici decat elementul curent in pozitia corespunzatoare
            while j >= gap and arr[j - gap] > current:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = current
        # reducerea distantei de sortare
        gap //= 2
    return arr
    # memoreaza elementul curent

def heapSort(arr):
    # construieste max-heap-ul din lista de elemente
    buildMaxHeap(arr)
    # extrage elementele unul cate unul din max-heap si le adauga in lista sortata
    sortedArr = []
    for i in range(len(arr)):
        sortedArr.append(arr[0])
        # elimina elementul maxim din max-heap si reconstruieste heap-ul
        arr[0] = arr[-1]
        arr.pop()
        maxHeapify(arr, 0)
    return sortedArr

def buildMaxHeap(arr):
    # construieste max-heap-ul din lista de elemente
    for i in range(len(arr)//2, -1, -1):
        maxHeapify(arr, i)

def maxHeapify(arr, i):
    # face ca nodul i sa respecte proprietatea de max-heap
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < len(arr) and arr[left] > arr[largest]:
        largest = left
    if right < len(arr) and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, largest)

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        left = []
        right = []
        for i in range(len(arr)-1):
            if arr[i] <= pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quickSort(left) + [pivot] + quickSort(right)

def countingSort(arr):
    # determina numarul maxim de elemente din lista
    k = max(arr) + 1
    # initializeaza vectorul auxiliar cu 0
    count = [0] * k
    # numara frecventa fiecarui element din lista
    for i in arr:
        count[i] += 1
    # acumuleaza numarul de elemente mai mici sau egale cu fiecare element din lista
    for i in range(1, k):
        count[i] += count[i-1]
    # construieste lista sortata
    sortedArr = [0] * len(arr)
    for i in arr:
        sortedArr[count[i]-1] = i
        count[i] -= 1
    return sortedArr

import random
import time
import sys
sys.setrecursionlimit(10**6)

# Generam liste aleatorii de diferite dimensiuni
list_100 = [random.randint(1, 100) for i in range(100)]
list_1000 = [random.randint(1, 1000) for i in range(1000)]
list_10000 = [random.randint(1, 10000) for i in range(10000)]

# Sortam fiecare listă cu fiecare algoritm și înregistram timpul de sortare

print("\n\nLista cu 100 elemente:\n")
start_time = time.time()
sortedArr = radixSort(list_100)
print("RadixSort pentru lista cu 100 elemente: ", time.time() - start_time)

start_time = time.time()
sortedArr = mergeSort(list_100)
print("MergeSort pentru lista cu 100 elemente: ", time.time() - start_time)

start_time = time.time()
sortedArr = shellSort(list_100)
print("ShellSort pentru lista cu 100 elemente: ", time.time() - start_time)

start_time = time.time()
sortedArr = quickSort(list_100)
print("QuickSort pentru lista cu 100 elemente: ", time.time() - start_time)

start_time = time.time()
sortedArr = countingSort(list_100)
print("CountingSort pentru lista cu 100 elemente: ", time.time() - start_time)

start_time = time.time()
sortedArr = sorted(list_100)
print("Sortarea nativă pentru lista cu 100 elemente: ", time.time() - start_time)


print("\n\nLista cu 1000 elemente:\n")
start_time = time.time()
sortedArr = radixSort(list_1000)
print("RadixSort pentru lista cu 1000 elemente: ", time.time() - start_time)

start_time = time.time()
sortedArr = mergeSort(list_1000)
print("MergeSort pentru lista cu 1000 elemente: ", time.time() - start_time)

start_time = time.time()
sortedArr = shellSort(list_1000)
print("ShellSort pentru lista cu 1000 elemente: ", time.time() - start_time)

start_time = time.time()
sortedArr = quickSort(list_1000)
print("QuickSort pentru lista cu 1000 elemente: ", time.time() - start_time)

start_time = time.time()
sortedArr = countingSort(list_1000)
print("CountingSort pentru lista cu 1000 elemente: ", time.time() - start_time)

start_time = time.time()
sortedArr = sorted(list_1000)
print("Sortarea nativă pentru lista cu 1000 elemente: ", time.time() - start_time)


print("\n\nLista cu 10000 elemente:\n")
start_time = time.time()
sortedArr = radixSort(list_10000)
print("RadixSort pentru lista cu 10000 elemente: ", time.time() - start_time)

start_time = time.time()
sortedArr = mergeSort(list_10000)
print("MergeSort pentru lista cu 10000 elemente: ", time.time() - start_time)

start_time = time.time()
sortedArr = shellSort(list_10000)
print("ShellSort pentru lista cu 10000 elemente: ", time.time() - start_time)

start_time = time.time()
sortedArr = quickSort(list_10000)
print("QuickSort pentru lista cu 10000 elemente: ", time.time() - start_time)

start_time = time.time()
sortedArr = countingSort(list_10000)
print("CountingSort pentru lista cu 10000 elemente: ", time.time() - start_time)

start_time = time.time()
sortedArr = sorted(list_10000)
print("Sortarea nativă pentru lista cu 10000 elemente: ", time.time() - start_time)

#Unul dintre testele pe care le-am rulat este acesta:
    #Lista cu 100 elemente:

    #RadixSort pentru lista cu 100 elemente:  0.0
    #MergeSort pentru lista cu 100 elemente:  0.0
    #ShellSort pentru lista cu 100 elemente:  0.0
    #QuickSort pentru lista cu 100 elemente:  0.0
    #CountingSort pentru lista cu 100 elemente:  0.0
    #Sortarea nativă pentru lista cu 100 elemente:  0.0


    #Lista cu 1000 elemente:

    #RadixSort pentru lista cu 1000 elemente:  0.0010044574737548828      
    #MergeSort pentru lista cu 1000 elemente:  0.002998828887939453       
    #ShellSort pentru lista cu 1000 elemente:  0.0029973983764648438      
    #QuickSort pentru lista cu 1000 elemente:  0.07551717758178711
    #CountingSort pentru lista cu 1000 elemente:  0.0010035037994384766   
    #Sortarea nativă pentru lista cu 1000 elemente:  0.0


    #Lista cu 10000 elemente:

    #RadixSort pentru lista cu 10000 elemente:  0.01201176643371582       
    #MergeSort pentru lista cu 10000 elemente:  0.04800772666931152
    #ShellSort pentru lista cu 10000 elemente:  0.057502031326293945
    #QuickSort pentru lista cu 10000 elemente:  6.315034866333008
    #CountingSort pentru lista cu 10000 elemente:  0.0025544166564941406  
    #Sortarea nativă pentru lista cu 10000 elemente:  0.0

# Se poate observa ca limbajul de programare python are o functie predefinita de sortare extrem de rapida, 
# iar algoritmul QuickSort desi este numit "Quick", este cel mai slab din punct de vedere al complexitatii timp dintre
# toate metodele de sortare prezentate.  