class Solution:
    def isHappy(self, n: int) -> bool:
        s = 0
        d = str(n)
        dic = {}
        while s != 1:
            s = 0
            for num in d:
                s += int(num)**2
            if s in dic:
                return False
            dic[s] = True
            d = str(s)
        return True