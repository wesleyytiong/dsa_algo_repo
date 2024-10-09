class Solution(object):
    def isAnagram(self, s, t):
    #Time Complexity: O(m+n), Space Complexity O(m+n) where m and n are the length of s and t, respectively
        #first check if count of s and t are the same, if not, then they cannot be anagrams
        if len(s) != len(t):
            return False
        
        #initilize the dictionaries to count frequency of characters in both strings s and t
        countS, countT = {}, {}
        
        #Iterate through and populate frequency in dictionaries
        for char in range(len(s)):
            countS[s[char]] = countS.get(s[char], 0) + 1 #account for if the character is not in the list
            countT[t[char]] = countT.get(t[char], 0) + 1
        #compare character frequencies in both dictionaries
        for char in countS:
            if countS[char] != countT.get(char, 0):
                return False
        return True #valid anagram
    
#Instantiate the solution class
sol = Solution()

#Test cases   
print(sol.isAnagram("anagram", "nagaram"))
print(sol.isAnagram("rat", "car"))