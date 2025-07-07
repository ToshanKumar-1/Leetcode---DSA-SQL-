class Solution(object):
    def arrangeCoins(self, n):

        if n == 1:
            return 1
        
        low, high = 0, n-1
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if (mid * (mid+1)// 2) <= n:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
        