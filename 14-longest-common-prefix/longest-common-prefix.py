class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        n = len(strs)
        ans = ""

        for i in range(len(strs[0])):
            if strs[0][i] == strs[n-1][i]:
                ans += strs[0][i]
            else:
                return ans
        
        return ans

                
        

        