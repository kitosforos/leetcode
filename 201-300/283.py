class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i, n in enumerate(nums):
            if n != 0:
                nums[count], nums[i] = nums[i], nums[count]
                count += 1
            