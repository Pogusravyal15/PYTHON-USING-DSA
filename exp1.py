#Write a python program to print Fibonacci series using recursion function.
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
n = int(input("Enter a number: "))
for i in range(n):
    print(fibonacci_recursive(i), end=" ")
