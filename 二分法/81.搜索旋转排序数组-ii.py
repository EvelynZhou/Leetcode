#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums)-1
        while(left<=right):
            mid = left+(right-left)//2
            if nums[mid]==target:
                return True
            if nums[left]==nums[mid]:
                # 无法判断哪个区间是递增的
                left+=1
            elif nums[left]<=nums[mid]:
                # 左区间是递增的
                if nums[left]<=target and nums[mid]>target:
                    right=mid-1
                else:
                    left = mid+1
            else:
                # 右区间是递增的
                if nums[mid]<target and nums[right]>=target:
                    left=mid+1
                else:
                    right=mid-1
        return False
                

# @lc code=end

