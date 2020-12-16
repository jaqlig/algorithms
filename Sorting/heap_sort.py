from random import randint

def heapSort(array):
    ptr = -1
    heap_arr = [None] * len(array)
    sorted = []

    def parentNode(index):
        if index == 0:
            return 0
        return int((index-1)/2)

    for i in array:
        ptr += 1
        heap_arr[ptr] = i

        heapify_ptr = ptr
        while(heapify_ptr != 0):
            if(heap_arr[parentNode(heapify_ptr)] < heap_arr[heapify_ptr]):
                heap_arr[parentNode(heapify_ptr)], heap_arr[heapify_ptr] = heap_arr[heapify_ptr], heap_arr[parentNode(heapify_ptr)]
                heapify_ptr = parentNode(heapify_ptr)
            else:
                break

    for i in heap_arr:      
        sorted.append(heap_arr[0])
        heap_arr[0] = heap_arr[ptr]
        heap_arr[ptr] = None
        ptr -= 1

        deheap_ptr = 0
        while(deheap_ptr != ptr):    
            try:
                if  heap_arr[deheap_ptr] < heap_arr[2*deheap_ptr+1] <= heap_arr[2*deheap_ptr+2]:
                    heap_arr[deheap_ptr], heap_arr[2*deheap_ptr+2] = heap_arr[2*deheap_ptr+2], heap_arr[deheap_ptr]
                    deheap_ptr = 2*deheap_ptr+2
                elif heap_arr[deheap_ptr] < heap_arr[2*deheap_ptr+1]:
                    heap_arr[deheap_ptr], heap_arr[2*deheap_ptr+1] = heap_arr[2*deheap_ptr+1], heap_arr[deheap_ptr]
                    deheap_ptr = 2*deheap_ptr+1
                else:
                    break
            except:
                pass
            try:
                if heap_arr[deheap_ptr] < heap_arr[2*deheap_ptr+1]:
                    heap_arr[deheap_ptr], heap_arr[2*deheap_ptr+1] = heap_arr[2*deheap_ptr+1], heap_arr[deheap_ptr]
                    deheap_ptr = 2*deheap_ptr+1
                else:
                    break
            except:
                break

    sorted.reverse()
    return sorted 

array = []
for i in range(50):
    array.append(randint(0,1000))

print(heapSort(array))
