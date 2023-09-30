class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        nser=list()
        for i in range(len(strs)):
            if strs[i]==False:
                continue
            else:
                temp=[]
                test=sorted(strs[i])
                temp.append(strs[i])
            for j in range(i+1,len(strs)):
                if strs[j] == False:
                    continue
                else:
                    compt=sorted(strs[j])
                    if compt==test:
                        temp.append(strs[j])
                        strs[j]=False
            nser.append(temp)
        return(nser)
