#INSERTION SORT
def insertion_sort(arr):
    n= len(arr)

    #traverse through all elements in the array starting from the second element
    for i in range(1,n):
        key =arr[i]

        #move elements of arr[0..i-1] that are greater than key to one position ahead of their current position
        j=i-1
        while j>=0 and key< arr[j]:
            arr[j+1]=arr[j]
            j -=1

        arr[j+1]=key

#example usage:
my_list= [64, 34, 25, 12, 22, 11, 90]

print("Original List:", my_list)
insertion_sort(my_list)
print("Sorted List:", my_list)

