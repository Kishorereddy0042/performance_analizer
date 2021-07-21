def bubblesort(arr):
    swaphappened=True
    while swaphappened:
        swaphappened = False
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                swaphappened=True
            
    #print(f"Total number of steps taken for bubble sort is {stp} of length {len(arr)}")
    return(arr)


def selectionsort(arr):
    itr=0
    while itr< len(arr):
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]

        itr+=1
    #print(f"Total number of steps taken for selection sort is {stp} of length {len(arr)}")
    return arr


def mergesort(arr):
    def merge_sorted(arr1,arr2):
        sorted_arr = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                sorted_arr.append(arr1[i])
                i += 1
            else:
                sorted_arr.append(arr2[j])
                j += 1
        while i < len(arr1):
            sorted_arr.append(arr1[i])
            i += 1
        while j < len(arr2):
            sorted_arr.append(arr2[j])
            j += 1
        return sorted_arr

    def divide_arr(arr):
        if len(arr) < 2:
            return arr[:]
        else:
            middle = len(arr)//2
            l1 = divide_arr(arr[:middle])
            l2 = divide_arr(arr[middle:])
            return merge_sorted(l1, l2)

    divide_arr(arr)

def quicksort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot=arr[-1]
        smaller,equal,larger=[],[],[]
        for num in arr:
            if num<pivot:
                smaller.append(num)
            elif num==pivot:
                equal.append(num)
            else: larger.append(num)
        return quicksort(smaller)+equal+quicksort(larger)