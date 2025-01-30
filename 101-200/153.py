class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        if (len(nums) == 1):
            return nums[0]
        while l <= r:
            mid = (l + r) // 2

            if nums[(mid - 1) % len(nums)] > nums[mid]:
                return nums[mid]
            if nums[(l - 1) % len(nums)] > nums[l]:
                return nums[l]
            elif nums[l] > nums[mid]:
                r = mid - 1
            else:
                l = mid + 1