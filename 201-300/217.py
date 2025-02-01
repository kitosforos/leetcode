class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        setnums = set()

        for num in nums:
            if num in setnums:
                return True
            setnums.add(num)
        return False