#https://leetcode-cn.com/problems/queries-on-number-of-points-inside-a-circle/
class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        res = []
        for cx, cy, r in queries:
            res.append(0)
            for x, y in points:
                if (x - cx) ** 2 + (y - cy) ** 2 <= r ** 2:
                    res[-1] += 1
        
        return res
		
		
points =[[1,1],[2,2],[3,3],[4,4],[5,5]]
queries=[[1,2,2],[2,2,2],[4,3,2],[4,3,3]]

sol = Solution()
result=sol.countPoints(points, queries)
#should be [2,3,2,4]
print(result)

