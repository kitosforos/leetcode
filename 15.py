class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sn = sorted(nums)
        res = []
        index = 0
        while index < len(sn):
            if index > 0 and sn[index - 1] == sn[index]:
                index += 1
                continue
            first = sn[index]
            i = index + 1
            j = len(sn) - 1
            while (i < j):
                if first + sn[i] + sn[j] == 0:
                    res.append([first, sn[i], sn[j]])
                    i += 1
                    while sn[i] == sn[i - 1] and i < j:
                        i += 1
                elif first + sn[i] + sn[j] > 0:
                    j -= 1
                else:
                    i += 1
            index += 1
        return res
            