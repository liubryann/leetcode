class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i = 0
        while i <= len(nums) - 1:
            j = i + 1
            while j <= len(nums) -1 and nums[j] == nums[i]:
                nums.remove(nums[j])
            i += 1
    
        return len(nums)
