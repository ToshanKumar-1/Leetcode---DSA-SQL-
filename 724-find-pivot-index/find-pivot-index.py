class Solution(object):
    def pivotIndex(self, nums):
        idx = -1
        n = len(nums)

        for i in range(0, n):
            if sum(nums[:i]) == sum(nums[i+1:]):
                idx = i
                break
            
        return idx
        