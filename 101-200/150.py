class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for t in tokens:
            if t.isdigit() or (t[0] == '-' and t[1:].isdigit()):
                stack.append(int(t))
            else:
                n = stack.pop()
                m = stack.pop()
                if t == "+":
                    res = (m + n)
                if t == "-":
                    res = (m - n)
                if t == "/":
                    res = int(m / float(n) if m * n > 0 else -(abs(m) / abs(n)))
                if t == "*":
                    res = (m * n)
                stack.append(res)
        return stack[0]