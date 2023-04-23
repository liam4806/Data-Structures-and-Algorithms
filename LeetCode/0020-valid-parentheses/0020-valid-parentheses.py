class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i == "(":
                stack.append(1)
            elif i == ")":
                if len(stack)==0 or stack[-1]!=1:
                    return False
                else:
                    stack.pop()
            elif i == "{":
                stack.append(2)
            elif i == "}":
                if len(stack)==0 or stack[-1]!=2:
                    return False
                else:
                    stack.pop()
            elif i == "[":
                stack.append(3)
            elif i == "]":
                if len(stack)==0 or stack[-1]!=3:
                    return False
                else:
                    stack.pop()
        if len(stack)==0:
            return True
        else:
            return False