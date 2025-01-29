class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        count = defaultdict(int)
        start, end = 0, 0
        while end < len(s):
            if s[end] in count and count[s[end]] >= start:
                start = count[s[end]] + 1
            count[s[end]] = end
            longest = max(longest, (end - start) + 1)
            end += 1
        return longest