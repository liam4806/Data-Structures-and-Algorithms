class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid-1]>nums[mid]:
                l=mid
                break
            elif nums[l]<nums[r]:
                break
            elif nums[l] > nums[mid]:
                r=mid-1
            elif nums[r] < nums[mid]:
                l=mid+1
            else:
                l=mid
                break
        r=len(nums)-1
        if target > nums[r]:
            r=l
            l=0
        elif target < nums[r]:
            l=l
        else:
            if target == nums[r]:
                return r
            else:
                return -1
        while l<=r:
            mid=(l+r)//2
            if target < nums[mid]:
                r=mid-1
            elif target > nums[mid]:
                l=mid+1
            else:
                return mid
        return -1
        