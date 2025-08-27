#https://leetcode-cn.com/problems/maximum-distance-between-a-pair-of-values/
#https://zhuanlan.zhihu.com/p/472121026,leetcode 1855.下标对中的最大距离
#annoying "indentation" error fixed by changing tab to space

class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(nums1)):
            j = i
            while j < len(nums2) and nums1[i] <= nums2[j]:
                j += 1
            res = max(res, j-i-1)

    
        return res
        
sol = Solution()
nums1,nums2 = [55,30,5,4,2],[100,20,10,10,5]
result=sol.maxDistance(nums1,nums2)
#expected output
#2
print(result)