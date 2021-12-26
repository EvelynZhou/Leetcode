#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        right=x
        left = 0
        if x==1:
            return x
        while(left<right-1):
            mid = left+(right-left)//2
            val = mid**2
            if val==x:
                return mid
            elif val<x:
                left=mid
            else:
                right=mid
        return left


# @lc code=end

