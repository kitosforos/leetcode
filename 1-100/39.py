class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtracking(ini, target, nums):

            if target == 0:
                res.append(nums[:])
                return 

            for i in range(ini, len(candidates)):
                if target - candidates[i] >= 0:
                    nums.append(candidates[i])
                    backtracking(i, target - candidates[i], nums)
                    nums.pop()

        backtracking(0, target, [])
        return res