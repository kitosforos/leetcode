class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        if (n == 0):
            return ""
        lcp = strs[0]
        for word in strs[1:]:
            while word.startswith(lcp) is not True:
                lcp = lcp[:-1]
                if not lcp:
                    return ""
        return lcp
                