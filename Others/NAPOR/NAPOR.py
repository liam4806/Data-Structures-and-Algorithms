import sys
l=list()
count=int(sys.stdin.readline().rstrip())
c=0
while c!=count:
    line=sys.stdin.readline().rstrip()
    for char in line:
        try:
            char=int(char)
        except:
            line=line.replace(char,' ')
    stor=line.split()
    for i in stor:
        if i[0]=='0' and len(i)>1:
            while True:
                if i[-1]=='0' and len(i)==1:
                    break
                elif i[0]!='0':
                    break
                i=i[1:]
        l.append(int(i))
    c+=1
l.sort()
print(*l)
