"""
    Practice Problem #1 Valid Parentheses:
    Given string s containing just the characters
    '(', ')','{','}', '[',']', determine if the input string is valid
    An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        #initialize stack as empty list to keep track of open brackets 
        stack = []
        
        #initialize dictionary to map close brackets to corresponding open bracket
        closeToOpen = {"}": "{", "]": "[", ")": "("}

        #iterate through each character in string s
        for char in s:
            #condition if character is close bracket
            if char in closeToOpen:
                #compare last value of non-empty stack to corresponding close bracket
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            #condition if character is open bracket
            else:
                stack.append(char)
        return True if not stack else False

# Create an instance of the Solution class
solution = Solution()

# Define an arbitrary string 's' containing brackets
s = "{[()]}"

# Call the isValid method and print the result
result = solution.isValid(s)
print(result)
