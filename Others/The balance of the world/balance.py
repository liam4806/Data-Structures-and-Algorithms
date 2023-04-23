import sys
def bal(se):
    stack=list()
    for i in se:
        if i=="(":
            stack.append(1)
        elif i==")":
            if len(stack)==0:
                return "no"
            else:
                if stack[-1]==2:
                    return "no" 
                elif stack[-1]==1:
                    stack.pop(-1)
        elif i=="[":
            stack.append(2)
        elif i=="]":
            if len(stack)==0:
                return "no"
            else:
                if stack[-1]==1:
                    return "no"
                elif stack[-1]==2:
                    stack.pop(-1)
    if len(stack)==0:
        return "yes"
    elif len(stack)>=1:
        return "no"
        
while True:
    se=sys.stdin.readline().rstrip()
    if se==".":
        break
    print(bal(se))
