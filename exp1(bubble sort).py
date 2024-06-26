#BUBBLE SORTING
def bubble_sort(arr):
    n=len(arr)

    #traverse through all elements in the array
    for i in range(n):
        #last i elements are already sorted, so we don't need to check them
        for j in range(0, n-i-1):
            #swap if the element found is greater than the next element
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]= arr[j+1], arr[j]

#example usage
my_list= [64, 34, 25, 12, 22, 11, 90]

print("Original List:", my_list)
bubble_sort(my_list)
print("Sorted List:", my_list)
