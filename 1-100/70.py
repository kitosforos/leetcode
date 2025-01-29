class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {}
        cache[1] = 1
        cache[2] = 2
        def function(num):
            if num in cache:
                return cache[num]
            else:
                cache[num] = function(num - 1) + function(num - 2)
                return cache[num]
            
        return function(n)