class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        dic = { "2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz"}
        
        def backtrack(ind, cur):
            if len(cur) == len(digits):
                res.append("".join(cur))
                return 
            if ind == len(digits):
                return
            for i in range(len(dic[digits[ind]])):
                cur.append(dic[digits[ind]][i])
                backtrack(ind + 1, cur)
                cur.pop()
        if len(digits) == 0:
            return []
        backtrack(0, [])
        return res