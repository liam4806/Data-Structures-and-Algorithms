class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        for i in s:
            if i == "(":
                stack.append(1)
            elif i == ")":
                try:
                    if stack[-1]==1:
                        stack.pop()
                    else:
                        stack.append(2)
                except:
                    stack.append(2)
        return len(stack)