class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sd = defaultdict(str)
        td = defaultdict(str)
        for i in (range(len(s))):
            if len(sd[s[i]]) > 0 and sd[s[i]] != t[i]:
                return False
            if len(td[t[i]]) > 0 and td[t[i]] != s[i]:
                return False
            sd[s[i]] = t[i]
            td[t[i]] = s[i]
        return True