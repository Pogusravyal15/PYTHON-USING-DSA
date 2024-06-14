def fun(n):
    if n<=0:
        return
    if(n%2==0):
        print(n+2)
    else:
        print(n+1)
    fun(n-1)
fun(5)