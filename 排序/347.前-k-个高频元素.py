#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums, k):
        nums_dict = {}
        for num in nums:
            if num not in nums_dict.keys():
                nums_dict[num]=1
            else:
                nums_dict[num]+=1
        nums_dict_n = sorted(nums_dict.items(), key=lambda x:(x[1]), reverse=True)
        indx = 0
        ans = []
        for t, _ in nums_dict_n:
            if indx>=k:
                break
            ans.append(t)
            indx +=1
        return ans


# @lc code=end

