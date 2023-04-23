a=list()
t=int(input())
for i in range(t):
    num=int(input())
    if num == 0:
        a.pop(-1)
    else:
        a.append(num)
print(sum(a))
