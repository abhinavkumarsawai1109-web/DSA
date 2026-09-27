class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        freq={}
        low=0
        max_len=0
        zero=0
        for high in range(len(nums)):
            if nums[high]==0:
                zero+=1
            while zero>k:
                if nums[low]==0:
                    zero-=1
                low+=1
            max_len=max(max_len,high-low+1)
        return max_len
        