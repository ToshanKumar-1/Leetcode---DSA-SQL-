class Solution(object):
    def countBits(self, n):
        ans = []
        for i in range(n+1):
            bn = bin(i)
            ans.append(bn.count('1'))

        return ans
        