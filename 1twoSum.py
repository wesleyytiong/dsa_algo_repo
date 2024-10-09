class Solution(object):
    def twoSum(self, nums, target):

    #Solution 1: Time Complexity O(n^2), where n is length of nums, Space Complexity O(1)
    #    for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[i]+nums[j] == target:
    #             return i, j #return the indices

    #Solution 2: Time Complexity O(n), Space Complexity O(n)
        
        dict = {} #initialize the dictionary
        for index in range(len(nums)):
            #complement + number = target
            complement = target - nums[index] 
            if complement in dict: #if result is in the dictionary
                return dict[complement], index # we're done, return the indices
            else: #otherwise, add it to the dictionary
                dict[nums[index]] = index

#Instantiate the solution class
sol = Solution()

#Test Cases
print(sol.twoSum([2,7,11,15],9))#[0,1]
print(sol.twoSum([3,2,4],6))#[1,2]
print(sol.twoSum([3,3],6)) #[0,1]
