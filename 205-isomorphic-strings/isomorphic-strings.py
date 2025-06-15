class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        dict1 = {}
        dict2 = {}

        for one, two in zip(s, t):
            if one in dict1:
                if dict1[one] != two:
                    return False
            else:
                dict1[one] = two
                
            if two in dict2:
                if dict2[two] != one:
                    return False
            else:
                dict2[two] = one

        return True

