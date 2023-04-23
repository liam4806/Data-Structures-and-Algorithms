m=int(input())

for n in range(1,m):
    t=0
    for i in range(len(str(n))):
        t=t+int(str(n)[i])
    x=n+t
    if x==m:
        print(n)
        exit()
    

print(0)
