from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}  
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        
        heap = []
        for key in freq:
            if len(heap) >= k:
                heapq.heappushpop(heap, (freq[key], key))
            else:
                heapq.heappush(heap, (freq[key], key))
                
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res 
        
