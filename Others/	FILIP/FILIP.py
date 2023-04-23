e=""
o=""
a,b=input().split()
for i in a:
    e=i+e 
for i in b:
    o=i+o 
if int(e)> int(o):
    print(e)
elif int(e)<int(o):
    print(o)
