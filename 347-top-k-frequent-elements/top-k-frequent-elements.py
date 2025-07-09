from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        cnt = Counter(nums)
        ans =  cnt.most_common(k)
        return [a[0] for a in ans]
        
        