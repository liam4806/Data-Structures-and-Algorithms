c=0
alpha=input()
cro=["c=","c-",'dz=','d-','lj','nj','s=','z=']
while True:
    d=0
    for i in cro:
        if i in alpha:
            c=c+1
            alpha=alpha.replace(i,"*")
        elif i not in alpha:
            d=d+1
    if d==8:
        break
print(len(alpha))
