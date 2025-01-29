class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        i = 0
        size = len(s)
        while (i < size):
            if s[i] == 'I':
                if i + 1 < size and s[i + 1] == 'V':
                    num += 4
                    i += 1
                elif i + 1 < size and s[i + 1] == 'X':
                    num += 9
                    i += 1
                else:
                    num += 1
            elif s[i] == 'X':
                if i + 1 < size and s[i + 1] == 'L':
                    num += 40
                    i += 1
                elif i + 1 < size and s[i + 1] == 'C':
                    num += 90
                    i += 1
                else:
                    num += 10
            elif s[i] == 'C':
                if i + 1 < size and s[i + 1] == 'D':
                    num += 400
                    i += 1
                elif i + 1 < size and s[i + 1] == 'M':
                    num += 900
                    i += 1
                else:
                    num += 100
            elif s[i] == 'V':
                num += 5
            elif s[i] == 'L':
                num += 50
            elif s[i] == 'D':
                num += 500
            elif s[i] == 'M':
                num += 1000
            i += 1
        
        return num