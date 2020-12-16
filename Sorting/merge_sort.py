from random import randint

def merge(array, l, mid, r):
 
    q1 = []
    q2 = []
  
    for i in range(l , mid + 1): 
        q1.append(array[i]) 
  
    for i in range(mid, r):
        q2.append(array[i+1])

    i = l

    while q1 and q2:
        if q1[0] < q2[0]:
            array[i] = q1.pop(0)
            i += 1
        else:
            array[i] = q2.pop(0)
            i += 1

    while q1:
        array[i] = q1.pop(0)
        i += 1        
    while q2:
        array[i] = q2.pop(0)
        i += 1

    return array   

def mergeSort(array, l, r):
    if l < r:
        mid = (l+r) // 2
        mergeSort(array, l, mid)
        mergeSort(array, mid+1, r)
        merge(array, l, mid, r)
    return array

array = []
for i in range(50):
    array.append(randint(0,1000))

print(mergeSort(array, 0, len(array)-1))
