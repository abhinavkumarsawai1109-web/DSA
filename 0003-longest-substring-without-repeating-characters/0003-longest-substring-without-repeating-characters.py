class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq={}
        low=0
        max_len=0
        for i in range(len(s)):
            freq[s[i]]=freq.get(s[i],0)+1
            while freq[s[i]]>1:
                freq[s[low]]-=1
                if freq[s[low]]==0:
                    del freq[s[low]]
                low+=1
            max_len=max(max_len,i-low+1)
        return max_len      
        