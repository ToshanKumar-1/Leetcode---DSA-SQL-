class Solution(object):
    def climbStairs(self, n):
        dp = [-1] * (n+1)

        def stairs(n, dp):
            if n == 0 or n == 1:
                return 1
            if dp[n] != -1:
                return dp[n]
            
            dp[n] = stairs(n-1, dp) + stairs(n-2, dp)
            return dp[n]

        ans = stairs(n, dp)
        return ans
        