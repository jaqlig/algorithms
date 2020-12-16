from random import randint

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(i):
            if array[j] > array[i]:
                array[j], array[i] = array[i], array[j]
    return array


array = []
for i in range(50):
    array.append(randint(0,1000))

print(bubbleSort(array))