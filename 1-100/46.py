class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def backtrack(cur):
            if len(cur) == len(nums):
                res.append(list(cur))
                return 
            
            for i in range(len(nums)):
                if nums[i] not in cur:
                    cur.append(nums[i])
                    backtrack(cur)
                    cur.pop()
            
        backtrack([])
        return (res)

        