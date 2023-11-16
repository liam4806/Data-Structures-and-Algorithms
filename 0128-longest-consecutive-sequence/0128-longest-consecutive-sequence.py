class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        final = 0
        for num in numSet:
            if num - 1 not in numSet:  
                temp = num
                tempS = 1
                while temp + 1 in numSet: 
                    temp += 1
                    tempS += 1
                final = max(final, tempS)  
        return final