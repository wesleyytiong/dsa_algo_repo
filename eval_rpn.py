""" 
Evaluate Reverse Polish Notation
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #Initialize empty stack to store results
        stack = []
        for c in tokens:
            #Check if token is +,*,-,/ operater, pop 2 elements from stack, complete operation, and push result back to stack
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '*':
                stack.append(stack.pop()*stack.pop()) 
            elif c == '-':
                a,b = stack.pop(), stack.pop()
                stack.append(b-a) 
            elif c == '/':
                a,b = stack.pop(), stack.pop()
                stack.append(int(b/a)) #Ensure integer division, truncating result of operation towards zero
            else:
                #If token is number, convert it to an integer and push it onto stack
                stack.append(int(c))
        #Final result is only element left in the stack
        return stack[0]
    
#Instantiate Solution class
sol = Solution()
    
#Define RPN Expression as List of Tokens:
tokens = ["2", "1", "+", "3", "*"]
    
#Call evalRPN Method with Tokens
result = sol.evalRPN(tokens)
print(f"The result of the RPN expression {tokens} is: {result}")

#Time Complexity: Token list: O(n), Stack pop and push O(1), Arithmetic operations O(1)
#Total Time Complexity: O(n), Space complexity O(n), where n is number of tokens