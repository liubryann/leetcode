class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i = 0 
        res = 3**i
        while res <= n:
            if res == n:
                return True
            else:
                i+=1
                res = 3**i
        return False
        
