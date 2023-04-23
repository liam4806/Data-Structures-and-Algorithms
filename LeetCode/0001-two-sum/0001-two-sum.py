class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for m in range(len(nums)):
            for n in range(m+1,len(nums)):
                if m==n:
                    continue
                elif nums[m]+nums[n]==target:
                    return [m,n]