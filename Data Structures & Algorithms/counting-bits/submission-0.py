class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[0]*(n+1)
        if n==0:
            res[0]=0
            return res
        else:
            for i in range(1,n+1):
                res[0] = 0
                count = 0
                c=i
                while(c!=0):
                    d = c%2
                    if(d==1):
                        count+=1
                    c//=2
                res[i]=count
        return res
