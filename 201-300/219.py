class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l, r = 0, 0
        dup = set()

        while r < len(nums):
            if nums[r] in dup:
                return True

            dup.add(nums[r])

            if r >= k:
                dup.remove(nums[l])
                l += 1
            r += 1
        return False