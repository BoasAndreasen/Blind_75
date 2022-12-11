class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1 = {}
        d2 = {}

        for el in s:
            if el in d1:
                d1[el] += 1
            else:
                d1[el] = 1

        for el in t:
            if el in d2:
                d2[el] += 1
            else:
                d2[el] = 1

        return d1 == d2
