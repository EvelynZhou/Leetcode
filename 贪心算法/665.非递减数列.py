#
# @lc app=leetcode.cn id=665 lang=python3
#
# [665] 非递减数列
#

# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        ans = 0
        val = nums[0]
        for i in range(1, len(nums)):
            if ans==1:
                if nums[i]<val or nums[i]<nums[i-1]:
                    return False
                else:
                    val = nums[i]
            else:
                if nums[i]<nums[i-1]:
                    ans += 1
                    if i>1:
                        if nums[i-2]<=nums[i]:
                            val = nums[i]
                            continue
                        else:
                            val = nums[i-1]
                            continue
                    else:
                        val = nums[i]

        if ans>1:
            return False
        else:
            return True
# @lc code=end

