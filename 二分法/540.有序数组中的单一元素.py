#
# @lc app=leetcode.cn id=540 lang=python3
#
# [540] 有序数组中的单一元素
#

# @lc code=start
class Solution:
    # def singleNonDuplicate(self, nums: List[int]) -> int:
    def singleNonDuplicate(self, nums):
        if len(nums)==1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[-1]!=nums[-2]:
            if nums[-2]==nums[-3]:
                return nums[-1]
            else:
                return nums[-2]
        left=0
        right=len(nums)-2
        while(left<=right):
            mid=left+(right-left)//2
            if nums[mid]==nums[mid-1]:
                if (mid-1-left)%2==0:
                    left=mid+1
                else:
                    right=mid-2
            elif nums[mid]==nums[mid+1]:
                if (mid-left)%2==0:
                    left=mid+2
                else:
                    right=mid-1
            else:
                return nums[mid]
        return nums[left]


        # if len(nums)==1:
        #     return nums[0]
        # if nums[0]!=nums[1]:
        #     return nums[0]
        # if nums[-1]!=nums[-2]:
        #     if nums[-2]==nums[-3]:
        #         return nums[-1]
        #     else:
        #         return nums[-2]
        # left = 1
        # right = len(nums)//2
        # left = 1
        # right = len(nums)//2
        # while (left<=right):
        #     mid = left+(right-left)//2
        #     if nums[2*mid]!=nums[2*mid+1]:
        #         if nums[2*mid]==nums[2*mid-1]:
        #             right=mid
        #         else:
        #             return nums[2*mid]
        #     else:
        #         left=mid-1
        # return nums[right]
            

                    
if __name__=="__main__":
    sf=Solution()
    # x = [i//2 for i in range(2*87784)]
    x = [1,1,2,3,3,4,4,8,8]
    # x.remove(4325)
    y = sf.singleNonDuplicate(x)
    print(y)



# @lc code=end

