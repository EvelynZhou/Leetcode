#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        lenght = len(nums)
        right=lenght-1
        if len(nums)<1:
            return [-1,-1]
        if nums[left]==target:
            tmp = left
            while(tmp+1<lenght and nums[tmp+1]==target):
                tmp+=1
            return [left, tmp]
        if nums[right]==target:
            tmp=right
            while(tmp-1>=0 and nums[tmp-1]==target):
                tmp-=1
            return [tmp, right]

        while left<right-1 and nums[right]>target and nums[left]<target:
            mid = left + (right-left)//2
            if nums[mid]==target:
                ans = [mid,mid]
                tmp = mid
                while(tmp+1<lenght and nums[tmp+1]==target):
                    tmp+=1
                ans[-1]=tmp
                tmp=mid
                while(tmp-1>=0 and nums[tmp-1]==target):
                    tmp-=1
                ans[0]=tmp
                return ans
            elif nums[mid]>target:
                right=mid
            else:
                left=mid
        return [-1, -1]
# @lc code=end

