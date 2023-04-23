class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        qu=[]
        for i in range(1,n+1):
            qu.append(i)
        count=0
        pointer=-1
        leng=n
        while leng!=1:
            while count<k:
                pointer=pointer+1
                if pointer == leng:
                    pointer=0
                count+=1
            if qu[pointer]==qu[-1]:
                del qu[pointer]
                pointer=0
                count=1
            else:
                del qu[pointer]
                count=1
            leng=leng-1
        return qu[0]