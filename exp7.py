#write a python program to print an list using recursion
def fun(l,i,s):
    if(i==len(l)):
        return s
    s+=l[i]
    return fun(l,i+1,s)
print(fun([1,2,3],0,0))