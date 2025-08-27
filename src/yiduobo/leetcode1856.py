#https://leetcode-cn.com/problems/maximum-subarray-min-product/
#https://zhuanlan.zhihu.com/p/472121773,leetcode 1856.子数组最小乘积的最大值

class Solution(object):
    def maxSumMinProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        stack = []
        left_pos = []
        for index in range(n):
            while stack and nums[stack[-1]] >= nums[index]:
                stack.pop()
            if not stack:
                left_pos.append(-1)
            else:
                left_pos.append(stack[-1])
            stack.append(index)
        
        stack = []
        right_pos = []
        for index in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[index]:
                stack.pop()
            if not stack:
                right_pos.append(n)
            else:
                right_pos.append(stack[-1])
            stack.append(index)
        right_pos.reverse()

        mod = 10 ** 9 + 7
        s = [nums[0]]
        for num in nums[1:]:
            s.append(s[-1] + num)

        res = 0
        for index in range(n):
            delta = s[right_pos[index] - 1]
            if left_pos[index] >= 0:
                delta -= s[left_pos[index]]
            res = max(res, nums[index] * delta)
        
        return res % mod
        
sol = Solution()
nums = [3,1,5,6,4,2]
result=sol.maxSumMinProduct(nums)
#expected output
#60
print(result)