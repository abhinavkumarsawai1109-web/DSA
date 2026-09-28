class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L=0
        cur_sum=0
        min_len=float('inf')
        for r in range(len(nums)):
            cur_sum+=nums[r]
            while cur_sum>=target:
                min_len=min(min_len,r-L+1)
                cur_sum-=nums[L]
                L+=1
        if min_len != float('inf'):
            return min_len
        else:
            return 0



        