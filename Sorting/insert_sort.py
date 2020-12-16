from random import randint

def insertSort(array):
    for i in range(len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
            j -= 1
    return array

array = []
for i in range(50):
    array.append(randint(0,1000))

print(insertSort(array))
