#https://leetcode-cn.com/problems/maximum-xor-for-each-query/


class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """

        res = []
        now = 0
        target = (1 << maximumBit) - 1
        for num in nums:
            now ^= num
            res.append(target ^ now)
        
        res.reverse()
        return res
		
s = Solution()
nums = [0,1,1,3]
maximumBit = 2
res = s.getMaximumXor(nums, maximumBit)
#output [0,3,2,3]
print(res)

nums = [0,1,2,2,5,7]
maximumBit = 3
res = s.getMaximumXor(nums, maximumBit)
#output [4,3,6,4,6,7]
print(res)

