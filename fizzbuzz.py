class Solution(object):
    def fizzBuzz(self, n):
        #Time Complexity O(n), Space Complexity O(n)
        answer = []
        for i in range(1, n+1 ):
        # Divisible by 3 and 5 
            if i % 3 ==0 and i % 5 ==0:
                answer.append('FizzBuzz')
        # Divisible by 3
            elif i % 3 == 0:
                answer.append('Fizz')
        # Divisible by 5
            elif i % 5 == 0:
                answer.append('Buzz')
        # Not divisible
            else:
                answer.append(str(i))
        return answer

#Instantiate the class
sol = Solution()
print(sol.fizzBuzz(3)) #['1', '2', 'Fizz']
print(sol.fizzBuzz(5)) #['1', '2', 'Fizz', '4', 'Buzz']
print(sol.fizzBuzz(15)) #['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']