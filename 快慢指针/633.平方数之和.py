#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#

# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        right = int(c**0.5)
        left = 0
        while(left<=right):
            val = left**2 + right**2
            if val>c:
                right-=1
            elif val<c:
                left+=1
            else:
                return True
        return False
# @lc code=end

