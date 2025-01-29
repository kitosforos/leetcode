class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        res = []
        
        def backtrack(i, cur, tot):
            if tot == target:
                res.append(list(cur))
                return
            
            if tot > target or i == len(candidates):
                return

            cur.append(candidates[i])
            backtrack(i + 1, cur, tot + candidates[i])
            cur.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            backtrack(i + 1, cur, tot)

        backtrack(0, [], 0)
        return (res)