class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        kv=defaultdict(int)
        for i in range(len(nums)):
            if kv[target-nums[i]]:
                return [i,kv[target-nums[i]]-1]
            kv[nums[i]]=i+1
