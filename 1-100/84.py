class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        maxSize = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxSize = max(maxSize, (i - index) * height)
                start = index
            stack.append((start, h))
        for i, h in stack:
            maxSize = max(maxSize, (len(heights) - i) * h)
        return maxSize