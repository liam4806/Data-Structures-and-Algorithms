a=set()
def d(n):
    num=0
    n=str(n)
    if len(n)==1:
        n="0"+n
    for i in n:
        num=num+int(i)
    x=int(n)+num
    return x
for i in range(10000):
    y=d(i)
    a.add(y)
for i in range(10000):
    if i not in a:
        print(i)
