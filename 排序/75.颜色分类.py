#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]
        for i in range(len(nums)):
            count[nums[i]]+=1
        index = 0
        for i in range(3):
            for j in range(count[i]):
                nums[index]=i
                index+=1
        
# @lc code=end

