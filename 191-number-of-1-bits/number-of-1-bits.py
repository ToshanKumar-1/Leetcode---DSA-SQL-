class Solution(object):
    def hammingWeight(self, n):
        ans = str(bin(n))
        return ans.count('1')
        