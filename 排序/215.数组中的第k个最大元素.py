#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums, k):
        left = 0
        right = len(nums)-1
        target = len(nums)-k
        while(left<=right):
            mid = self.quickSelection(nums, left, right)
            if mid==target:
                return nums[target]
            elif mid<target:
                left = mid+1
            else:
                right=mid-1

    def quickSelection(self, nums, left, right):
        val = nums[left]
        r = right
        l = left+1
        while(l<=r):
            while(nums[r]>=val and r>left):
                r-=1
            while(nums[l]<=val and l<right):
                l+=1
            if (l>=r):
                break
            else:
                tmp = nums[l]
                nums[l]=nums[r]
                nums[r] = tmp
        nums[left]=nums[r]
        nums[r]=val
        return r

if __name__=="__main__":
    x =  [7,6,5,4,3,2,1]
    k = 4
    sl = Solution()
    sl.findKthLargest(x, k)

# @lc code=end


