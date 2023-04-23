class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=list()
        count=0
        for i in logs:
            i=i.split("/")[0]
            if i == "..":
                try:
                    stack.pop()
                    count-=1
                except:
                    continue
            elif i == ".":
                continue
            else:
                stack.append(i)
                count+=1
        return count