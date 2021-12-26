#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        ans = nums[left]
        while (left<=right):
            mid = left + (right-left)//2
            if nums[mid]<ans:
                ans=nums[mid]
            if nums[left]==nums[mid]:
                left+=1
            elif nums[left]<nums[mid]:
                # 左区间是递增区间
                if nums[left]<ans:
                    ans = nums[left]
                left = mid+1
            else:
                right = mid-1
        return ans


            
# @lc code=end

