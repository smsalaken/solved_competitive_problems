# https://leetcode.com/problems/two-sum/submissions/


# O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return([i,j])
                
            
# much better solution in terms of time complexity
# O(n) - using hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for j, num in enumerate(nums):
            complement = seen.get(target-num)
            if complement is not None:
                return([j, complement])
            seen[num] = j


a = "a1"
b = "b1"
a > b
b > a
a.isnumeric()
a.split(" ")[1].isnumeric()




## using two pointers
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums)-1
        
        sorted_nums = sorted(nums)
        
        while True:
            if ((sorted_nums[i] + sorted_nums[j]) == target):
                break
            if ((sorted_nums[i] + sorted_nums[j]) > target) :
                j = j - 1
            if ((sorted_nums[i] + sorted_nums[j]) < target) :
                i = i + 1 
            
        # print("i:{}, j:{}".format(i,j))
        ii = nums.index(sorted_nums[i])
        jj = nums.index(sorted_nums[j])
        
        if jj == ii: # duplicate items in original list
            jj = nums.index(sorted_nums[j], ii+1)
        
        return([ii,jj])