class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        stack=dict()
        for i in nums:
            try:
                if stack[i]==True:
                    return True
                else:
                    stack[i]=True
            except:
                stack[i]=True
        return False
