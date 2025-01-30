class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj = nums[0]
        counter = 1

        for num in nums[1:]:
            if counter == 0:
                maj = num
            counter += 1 if num == maj else -1
        return maj