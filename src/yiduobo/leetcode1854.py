#https://leetcode-cn.com/problems/maximum-population-year/
#https://zhuanlan.zhihu.com/p/471593881,leetcode 1854.人口最多的年份

class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """

        delta = {}
        for birth, death in logs:
            delta[birth] = delta.get(birth, 0) + 1
            delta[death] = delta.get(death, 0) - 1
        
        ma = 0
        res = None
        now = 0
        for y in range(1950, 2051):
            now += delta.get(y, 0)
            if now > ma:
                ma = now
                res = y
        
        return res
        
sol = Solution()
logs = [[1993,1999],[2000,2010]]
result=sol.maximumPopulation(logs)
#expected output
#1993
print(result)

logs = [[1950,1961],[1960,1971],[1970,1981]]
result=sol.maximumPopulation(logs)
#expected output
#1960
print(result)