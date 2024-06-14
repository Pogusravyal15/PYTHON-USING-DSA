#SELECTION SORT
def selection_sort(arr):
    n=len(arr)

    #traverse through all elements in the array
    for i in range(n):
        #find the minimum element in the unsorted part
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index= j

        #swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index]=arr[min_index], arr[i]

#example usage
my_list= [64, 34, 25, 12, 22, 11, 90]

print("Original List:", my_list)
selection_sort(my_list)
print("Sorted List:", my_list)

