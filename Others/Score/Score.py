import sys
x=int(input())
a=[str(sys.stdin.readline().rstrip()) for y in range(x)]
for i in range(x):
    total=0
    count=0
    for z in a[i]:
        if z == "O":
            count=count+1
            total=total+count
        else:
            count=0
    print(total)
