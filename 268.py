class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        if nums[-1] != len(nums):
            return len(nums) 
        elif nums[0] != 0:
            return 0 
        else:
            for i in range(1, len(nums)):
                if i != nums[i]:
                     return i
