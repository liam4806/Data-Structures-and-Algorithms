class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        acs=[1]
        for i in nums:
            acs.append(acs[-1]*i)
        des=[1]
        for i in nums[::-1]:
            des.append(des[-1]*i)
        newl=[]
        des=des[::-1]
        for i in range(len(acs)-1):
            newl.append(acs[i]*des[i+1])
        return newl