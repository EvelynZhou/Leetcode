#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        ans = 0
        left = prices[0]
        for i in range(1, len(prices)):
            if left<prices[i]:
                ans += (prices[i]-left)
                left=prices[i]
            else:
                left = min(left, prices[i])
        return ans
# @lc code=end

