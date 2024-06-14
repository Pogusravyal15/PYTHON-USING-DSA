#Write a python program to print n natural numbers in ascending order.
def print_numbers(n):
    if n > 0:
        print_numbers(n - 1) #This is called Tail Recursion, where the function is called after printing.
        print(n)
print_numbers(5)

#Write a python program to print n natural numbers in descending order.
def print_numbers(n):
    if n > 0:
        print(n)
        print_numbers(n - 1) #This is called Head Recursion, where the function is called before printing.
print_numbers(5)
