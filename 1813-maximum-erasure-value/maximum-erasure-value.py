class Solution(object):
    def maximumUniqueSubarray(self, nums):
        left, right = 0, 0
        maxsum, cursum = 0, 0
        seen = set()

        for i in range(len(nums)):
            cursum += nums[i]
            right += 1
            while nums[i] in seen:
                seen.remove(nums[left])
                cursum -= nums[left]
                left += 1

            seen.add(nums[i]) 
            maxsum = max(cursum, maxsum)
        return maxsum

        