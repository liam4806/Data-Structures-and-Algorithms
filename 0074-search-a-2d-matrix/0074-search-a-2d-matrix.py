class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target <= i[-1]:
                l=0
                r=len(i)-1
                while l<=r:
                    mid=(l+r)//2
                    if target > i[mid]:
                        l=mid+1
                    elif target < i[mid]:
                        r=mid-1
                    else:
                        return True
                return False
            else:
                continue
        return False