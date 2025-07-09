from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        # APPROACH - 1 Using Counter
        return Counter(s) == Counter(t)


        # APPROACH - 2

        # if len(s) != len(t):
        #     return False
        # count = [0] * 256

        # for i in range(len(s)):
        #     count[ord(s[i])] += 1
        #     count[ord(t[i])] -= 1
        
        # for cnt in count:
        #     if cnt != 0:
        #         return False
        # return True


