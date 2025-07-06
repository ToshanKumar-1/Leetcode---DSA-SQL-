class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        ln = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                break
            ln += 1
        return ln