class Solution(object):
    def isAnagram(self, s, T):
        """
        :type s: str
        :type T: str
        :rtype: bool
        """
        return sorted(s) == sorted(T)
