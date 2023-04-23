S=int(input())
for i in range(S):
    num,char = input().split()
    num=int(num)
    n=""
    for i in char:
        for t in range(num):
            n=n+i 
    print(n)
