from create_list import create_list_random

def bubble_sort(arr):
    sorted = True
    while sorted:
        sorted = False
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                sorted = True
                arr[i],arr[i+1] = arr[i+1],arr[i]
    return arr

#arr = create_list_random(1000)
#print(bubble_sort(arr))