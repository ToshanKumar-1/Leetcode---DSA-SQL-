class Solution(object):
    def pivotIndex(self, nums):
        tsum = sum(nums)
        lsum = 0

        for i in range(len(nums)):
            rsum = tsum - lsum - nums[i]
            if lsum == rsum:
                return i
            lsum += nums[i]

        return -1
        