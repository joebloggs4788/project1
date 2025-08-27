#每日leetcode 1888.使二进制字符串字符交替的最少反转次数,https://zhuanlan.zhihu.com/p/478444868
#https://leetcode-cn.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/


class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """

        odd_one = 0
        even_one = 0
        n = len(s)
        for index, char in enumerate(s):
            if char == '1':
                if index % 2 == 0:
                    even_one += 1
                else:
                    odd_one += 1

        res = min((n + 1) / 2 - even_one + odd_one, even_one + n / 2 - odd_one)

        for index in range(n - 1):
            odd_one, even_one = even_one, odd_one
            if s[index] == '1' and n & 1:
                odd_one -= 1
                even_one += 1
            
            res = min(res, (n + 1) / 2 - even_one + odd_one, even_one + n / 2 - odd_one)
        
        return res
        
sol = Solution()
s = "111000"
result=sol.minFlips(s)
#expected output
#2
print("%i" %(result))