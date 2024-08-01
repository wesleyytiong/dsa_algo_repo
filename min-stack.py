"""
Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.     
    
"""

class MinStack:

    #initialize two stacks
    def __init__(self):
        self.stack = [] #stack to store all elements
        self.minStack = [] #stack to keep track of min elements

    def push(self, val: int) -> None:
        self.stack.append(val)
        #compare min value in minStack and append to minStack O(1) time
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    #pop both stacks to ensure minStack reflects min value after pop O(1) time
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    #return top element in O(1) time
    def top(self) -> int:
        return self.stack[-1]

    #return min element in O(1) time
    def getMin(self) -> int:
        return self.minStack[-1]
        
    #Total Time Complexity O(1)
    #Total Space Complexity O(n)+O(n) = O(n)
    
# Create an instance of MinStack to test code
min_stack = MinStack()

# Push elements onto the stack
min_stack.push(1)
min_stack.push(3)
min_stack.push(-2)
min_stack.push(5)

# Test getMin, top, and pop methods
print(min_stack.getMin())  # Output: -2
print(min_stack.top())     # Output: 5
min_stack.pop()            # Remove 5
print(min_stack.getMin())  # Output: -2
print(min_stack.top())     # Output -2


    
    