#每日leetcode 1887.使数组元素相等的减少操作次数,https://zhuanlan.zhihu.com/p/477848438
#https://leetcode-cn.com/problems/reduction-operations-to-make-the-array-elements-equal/

class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        cnt_dict = {}
        for num in nums:
            cnt_dict[num] = cnt_dict.get(num, 0) + 1
        
        res = 0
        cnt = 0
        #for num in sorted(cnt_dict.keys(), reverse=True):
        #    res += cnt
        #    cnt += cnt_dict[num]
		
		#my method
        length = len(cnt_dict)
        i = 1
        new_cnt = sorted(cnt_dict.keys(), reverse=True)
        for key in new_cnt:
            res += cnt_dict[key]*(length-i)
            i += 1
        
        return res
        
sol = Solution()
nums = [1,1,2,2,3]
result=sol.reductionOperations(nums)
#expected output
#4
print(result)