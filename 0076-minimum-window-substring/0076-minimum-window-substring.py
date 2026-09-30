class Solution:
    def fun(self, have: list[int], need: list[int]) -> bool:
        for i in range(256):
            if have[i] < need[i]:
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        n,m=len(s),len(t)
        if n<m:
            return ""
        have=[0]*256
        need=[0]*256
        for char in t:
            need[ord(char)]+=1
        low=0
        res=float("inf")
        start=-1
        for high in range(n):
            have[ord(s[high])]+=1
            while self.fun(have,need):
                leng=high-low+1
                if res>leng:
                    res=leng
                    start=low
                have[ord(s[low])]-=1
                low+=1
        if res==float("inf"):
            return ""
        return s[start:start+res]



        