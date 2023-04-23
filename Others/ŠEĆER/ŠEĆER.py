def pack(n):
    count=0
    if n%5==0:
        return n//5
    elif n==3:
        return 1
    elif n<5:
        return -1
    
    a=n//5
    b=n%5
    while b%3!=0:
        b=b+5
        if b>n:
            return -1
        count=count+1
    x=b//3
    y=a-count
    return y+x

n=int(input())
ans=pack(n)
print(ans)
