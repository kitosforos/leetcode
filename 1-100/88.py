class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = 0, 0, 0
        ret = nums1[:m]
        while i < m or j < n:
            if j >= n or (i < m and ret[i] < nums2[j]):
                nums1[k] = ret[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1