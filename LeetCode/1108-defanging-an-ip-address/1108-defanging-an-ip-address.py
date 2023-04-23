class Solution:
    def defangIPaddr(self, address: str) -> str:
        output=address.split(".")
        y=len(output)
        x=""
        c=0
        for i in output:
            if c==y-1:
                x=x+i
                break
            x=x+i+"[.]"
            c=c+1
        
        return x