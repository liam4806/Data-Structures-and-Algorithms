from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=dict()
        frequency=list()
        for ele in nums:
            counter[ele]=counter.get(ele,0)+1
            if(len(frequency)<counter[ele]):
                frequency.append([ele])
            else:
                frequency[counter[ele]-1].append(ele)
        for i in range(len(frequency)-1,-1,-1):
            if len(frequency[i])==k:
                return frequency[i]
        