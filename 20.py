class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for b in s:
            if b == "(" or b == "[" or b == "{":
                stack.append(b)
            elif not stack:
                return False
            else:
                c = stack.pop()
                if b == ")" and c != "(":
                    return False
                if b == "]" and c != "[":
                    return False
                if b == "}" and c != "{":
                    return False
        return False if len(stack) else True