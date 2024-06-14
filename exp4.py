n=int(input("enter the numbers:"))
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print("reversed number:", rev)
if(rev%2==0):
    rev+=2
elif(rev%2!=0):
    rev+=1
else:
    pass
print("Final number:",rev)


