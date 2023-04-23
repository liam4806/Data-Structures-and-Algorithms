h,m = map(int, input().split())
if m-45 <0:
    if h-1==-1:
        h=23
    else:
        h=h-1
    t=m-45
    M=60+t
elif m-45>=0:
    M=m-45
print(h,M)
