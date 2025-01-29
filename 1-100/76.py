class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic_t = Counter(t)
        changed = False
        l, r = 0, 0
        ml, mr = 0, len(s)
        while r < len(s) and l <= r:
            if s[r] in dic_t and not changed:
                dic_t[s[r]] -= 1
            if max(dic_t.values()) <= 0:
                if mr - ml + 1 > r - l + 1:
                    ml = l
                    mr = r
                if s[l] in dic_t:
                    dic_t[s[l]] += 1
                l += 1
                changed = True
            else:
                r += 1
                changed = False
        return s[ml:mr + 1] if mr != len(s) else ""