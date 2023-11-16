class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store=defaultdict(list)
        for i in strs:
            alpha=[0]*26
            for s in i:
                alpha[ord(s)-ord('a')]+=1
            alpha=tuple(alpha)
            store[alpha].append(i)
        return store.values()