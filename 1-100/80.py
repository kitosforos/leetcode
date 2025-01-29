class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, 0
        while i < len(nums):
            num = nums[i]
            nums[j] = num
            i += 1
            j += 1
            if i < len(nums) and nums[i] == num:
                nums[j] = nums[i]
                j += 1
                i += 1
            while i < len(nums) and nums[i] == num:
                i += 1
        return j