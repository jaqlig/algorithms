from random import randint

def quickSort(array, l, r):
    if l < r:
        j = l
        for i in range(l,r):
            if array[i] < array[r]:
                array[i],array[j] = array[j],array[i]
                j += 1
        array[j],array[r] = array[r],array[j]
        quickSort(array, l, j-1)
        quickSort(array, j+1, r)
    return array

array = []
for i in range(50):
    array.append(randint(0,1000))

print(quickSort(array, 0, len(array)-1))
