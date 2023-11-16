class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_=list(s)
        t_=list(t)
        s_.sort()
        t_.sort()
        if s_ == t_:
            return True
        return False