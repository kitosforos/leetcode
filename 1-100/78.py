class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def backtracking(ini, cur):
            res.append(list(cur))

            for i in range(ini, len(nums)):
                cur.append(nums[i])
                backtracking(i + 1, cur)
                cur.pop()


        backtracking(0, [])
        return res
