import sys
def isTrue(ps):
    if "(" not in ps or ")" not in ps:
        return "NO"
    fcount=0
    lcount=0
    for t in ps:
        if t=="(":
            fcount+=1
        elif t==")":
            lcount+=1 
        if fcount<lcount:
            return "NO"
    if fcount==lcount:
        return "YES"
    else:
        return "NO"

count=0
x=int(sys.stdin.readline())
while count!=x:
    ps=sys.stdin.readline()
    print(isTrue(ps))
    count+=1
