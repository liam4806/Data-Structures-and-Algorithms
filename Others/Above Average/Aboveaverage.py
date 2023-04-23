import sys
number_of_students=int(input())
for i in range(number_of_students):
    count=0
    scores=list(map(int,sys.stdin.readline().split()))
    if len(scores)-1>scores[0]:
        print("Wrong input")
    newlist=scores[1:]
    ave=sum(newlist)/len(newlist)
    for i in newlist:
        if i>ave:
            count=count+1
    print(f"{count/scores[0]*100:.3f}%")
