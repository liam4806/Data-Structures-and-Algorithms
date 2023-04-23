class Solution:
    def firstUniqChar(self, s: str) -> int:
        flag=0
        dic=dict()
        indexstore=dict()
        x=len(s)
        for i in range(x):
            let=s[i]
            dic[let]=dic.get(let,0)+1
            if dic[let] ==1:
                indexstore[let]=(dic[let],i)
        for k,v in dic.items():
            tup=(k,v)
            if tup[1] == 1:
                ans=tup[0]
                return indexstore[ans][1]
                flag=1
                break
        if flag==0:
            return -1