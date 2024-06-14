#Printing an list in reverse order
l=[2,3,5,6,7,9,11]
for i in range(len(l)//2+1):
    l[i],l[-1-i]=l[-1-i],l[i]
print(l)

#printing an list in reverse using recursion
def reverse_list(lst):
    if not lst:
        return []
    return [lst[-1]] + reverse_list(lst[:-1])

l = [2,3,5,6,7,9,11]
reversed_list = reverse_list(l)
print("", reversed_list)
