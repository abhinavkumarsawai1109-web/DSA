class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        nums.sort()
        left=0
        right=1
        while right< len(nums):
            if(nums[left]==nums[right]):
                return nums[left]
            right+=1
            left+=1
        return -1

        