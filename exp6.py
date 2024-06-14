#Ascending Recursive
def fun(n,l):
    if n == 6:
        return l
    l.append(n)
    t=fun(n+1,l)
    return t

print(fun(1,[]))

#Desending Recursive
def fun(n, l):
    if n <= 0:
        return l
    l.append(n)
    t = fun(n-1, l)
    return t

print(fun(5, []))