class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd=dict()
        count=0
        if len(s)!= len(t):
            return False
        for i in s:
            try:
                sd[i]=sd[i]+1
            except:
                sd[i]=1
        for i in t:
            try:
                if sd[i]:
                    sd[i]=sd[i]-1
                elif sd[i]==0:
                    return False
                else:
                    return False
            except:
                return False
        return True
