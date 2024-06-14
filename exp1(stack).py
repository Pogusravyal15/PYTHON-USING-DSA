#STACK
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def size(self):
        return len(self.items)

# Example usage
stack = Stack()
print("Is the stack empty?", stack.is_empty())  # Output: True
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)
stack.push(9)
stack.push(10)
print("Stack:", stack.items)  # Output: [1, 2, 3]
print("Top of the stack:", stack.peek())  # Output: 3
print("Pop:", stack.pop())  # Output: 3 (corrected to call the method)
print("Stack after pop:", stack.items)  # Output: [1, 2]
print("Is the stack empty?", stack.is_empty())  # Output: False
print("Size of the stack:", stack.size())  # Output: 2