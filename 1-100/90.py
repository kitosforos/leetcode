class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(cur, ini):
            if cur not in res:
                res.append(list(cur))
            for i in range(ini, len(nums)):
                cur.append(nums[i])
                backtrack(cur, i + 1)
                cur.pop()
        
        backtrack([], 0)
        return (res)
        