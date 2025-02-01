class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        ptow = defaultdict(str)
        wtop = defaultdict(str)
        if len(pattern) != len(s.split()):
            return False
        for i, word in enumerate(s.split()):
            if pattern[i] not in ptow and word not in wtop:
                ptow[pattern[i]] = word
                wtop[word] = pattern[i]
            elif ptow[pattern[i]] != word or wtop[word] != pattern[i]:
                return False
        return True
        