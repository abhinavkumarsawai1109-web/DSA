class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        for i in nums:
            if i>0:
                pos.append(i*i)
            else:
                neg.append(i*i)
        neg.reverse()
        res=[]
        p=len(pos)
        n=len(neg)
        m=j=0
        while m<p and j<n:
            if pos[m]<neg[j]:
                 res.append(pos[m])
                 m+=1
            else:
                res.append(neg[j])
                j+=1
        while m<p:
            res.append(pos[m])
            m+=1
        while j<n:
            res.append(neg[j])
            j+=1
            
        return res



     
        