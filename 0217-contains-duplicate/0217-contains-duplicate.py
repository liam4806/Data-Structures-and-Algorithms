class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checkdict=defaultdict(int)
        for i in nums:
            if checkdict[i]:
                checkdict[i]+=1
                if checkdict[i]>=2:
                    return True
            else:
                checkdict[i]=1
        return False
        