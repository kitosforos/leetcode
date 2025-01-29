class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack) - len(needle)
        i = 0
        while (i <= n):
            if haystack[i:].startswith(needle):
                return i
            i += 1
        return -1
        