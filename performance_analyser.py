from sort_algorithims import bubblesort, mergesort, quicksort, selectionsort
import random, time

def random_list(size, max_value):
    ran_list=(random.randint(1,max_value) for num in range(size) )
    #print("This is type",type(ran_list))
    return ran_list

def performance_analizer(fun_name,arr):
    tic=time.time()
    res=fun_name(arr)
    toc=time.time()
    seconds=toc-tic
    print(f"{fun_name.__name__.capitalize()}\t--> Elapsed Time {seconds}")
    #and the sorted array is {res}

def main():
    #arr=[82,21,48,3,1,10,25,34,21]
    size=int(input("Please enter the size of random numbers to test: "))
    max_val=int(input("Please enter the max value of random numbers to test: "))
    l=list(random_list(size,max_val))
    performance_analizer(bubblesort,l.copy())
    performance_analizer(mergesort,l)
    performance_analizer(selectionsort,l)
    performance_analizer(quicksort,l)

if __name__=='__main__':
    main()