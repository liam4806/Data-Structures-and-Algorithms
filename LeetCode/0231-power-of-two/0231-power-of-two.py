class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1 or n==2:
            return True
        while True:
            n=n/2
            if n==2:
                return True
            elif n<2:
                return False
        

        