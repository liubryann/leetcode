class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict = {}
        list = []
        for i in nums1:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        
        for i in nums2:
            if i in dict and dict[i] > 0:
                list.append(i)
                dict[i] -= 1
            
        return list
