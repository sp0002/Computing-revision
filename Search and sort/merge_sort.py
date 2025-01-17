from create_list import create_list_random

def merge_sort(arr):
    if len(arr) > 1:
        half = len(arr)//2
        left = arr[:half]
        right = arr[half:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i<len(left) and j<len(right):
            if left[i] <right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k+=1
        while i<len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j<len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        return arr
    return arr
#arr = create_list_random(100)
#print(merge_sort(arr))
