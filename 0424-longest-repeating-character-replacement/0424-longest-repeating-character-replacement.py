class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq={}
        low=0
        max_len=0
        max_freq=0
        for high in range(len(s)):
            freq[s[high]]=freq.get(s[high],0)+1
            max_freq=max(max_freq,freq[s[high]])
            while (high-low+1)-max_freq>k:
                freq[s[low]]-=1
                low+=1
            max_len=max(max_len,high-low+1)
        return max_len


        




        