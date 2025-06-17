class Solution(object):
    def countLargestGroup(self, n):
        ans = [0] * 37

        for k in range(1, n+1):
            sm = 0
            i = k
            while i > 0:
                rem = i % 10
                sm += rem
                i //= 10
            ans[sm] += 1
        
        return ans.count(max(ans))
        