class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setofnums=set(nums)
        longest=0
        for i in nums:
            length=0
            if i-1 not in setofnums:
                while i+length in setofnums:
                    length+=1
                if length>longest:
                    longest=length
        return longest