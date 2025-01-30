class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        setNums = set(nums)
        longest = 0

        for n in setNums:
            if n - 1 not in setNums:
                l = 0
                while n + l in setNums:
                    l += 1
                longest = max(l, longest)
        return longest