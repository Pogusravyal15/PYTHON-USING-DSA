#write a python program to print sum of even numbers and odd numbers.
def fun(l,i,s1,s2):
    if(i==len(l)):
        return s1,s2
    if(l[i]%2==0):
        s1+=l[i]
    else:
        s2+=l[i]
    return fun(l,i+1,s1,s2)
print(fun([1,2,3,4,5,6],0,0,0))