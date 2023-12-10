class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid-1]>nums[mid]:
                return nums[mid]
            elif nums[l]<nums[r]:
                return nums[l]
            elif nums[l]>nums[mid]:
                r=mid-1
            elif nums[r]<nums[mid]:
                l=mid+1
            else:
                return nums[mid]           
        return 0
        
            