
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: list[int]
        :type target: int
        :return: list[tuple[2,int]]
        """
        
        res = []
        for idx1 in range(len(numbers)):
            for idx2 in range(idx1+1,len(numbers)):
                if target == numbers[idx1] + numbers[idx2]:
                    t = (idx1,idx2)
                    res.extend(t)
                    #res.extend((idx1,idx2))         
        
        return res
        
    def twoSum1(self, numbers, target):
        """
        :type numbers: list[int]
        :type target: int
        :return: list[tuple[2,int]]
        """
        
        res = []
        position_dict = {}
        for idx1 in range(len(numbers)):
            position_dict.update({numbers[idx1]:idx1})
        for idx1 in range(len(numbers)):
            if target - numbers[idx1] in position_dict:
                res.extend((idx1, position_dict.get(target - numbers[idx1])))
        return res
        
sol = Solution()
nums1 = [1,5,3,8,7,11,23,9]
target1 = 14
result=sol.twoSum1(nums1,target1)
#expected output
#2
print(result)