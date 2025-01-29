class Solution(object):
    def twoSum(self, nums, target):
        prevSet = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevSet:
                return [prevSet[diff], i]
            prevSet[n] = i 