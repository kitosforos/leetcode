class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        ntoi = defaultdict(int)
        for i, n in enumerate(numbers):
            if target - n in ntoi:
                return (ntoi[target - n] + 1, i + 1)
            ntoi[n] = i
        