#
# @lc app=leetcode.cn id=451 lang=python3
#
# [451] 根据字符出现频率排序
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        s_dict = {}
        for char in s:
            if char not in s_dict.keys():
                s_dict[char] = 1
            else:
                s_dict[char] += 1
        s_dict_sort = sorted(s_dict.items(), key=lambda x:(x[1]), reverse=True)
        ans = ""
        for k,v in s_dict_sort:
            for i in range(v):
                ans += k
        return ans

# @lc code=end

