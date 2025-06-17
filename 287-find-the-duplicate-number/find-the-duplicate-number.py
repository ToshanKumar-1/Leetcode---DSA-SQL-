class Solution(object):
    def findDuplicate(self, nums):
        ans = -1

        for i in range(len(nums)):
            idx = abs(nums[i])
            if nums[idx] < 0:
                ans = idx
                break
            nums[idx] = -1 * nums[idx]

        return ans        