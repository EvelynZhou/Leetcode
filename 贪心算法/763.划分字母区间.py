#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        s_dict = {}
        chara = list(set(list(s)))
        for i in range(len(chara)):
            start = s.find(chara[i])
            end = s.rfind(chara[i])
            s_dict[chara[i]]=[start, end]
        ans = []
        start = s_dict[s[0]][0]
        end = s_dict[s[0]][1]
        for i in range(0, len(s)):
            if i==end:
                ans.append(len(s[start:min(end+1, len(s))]))
                start = i+1
                if start==len(s):
                    return ans
                else:
                    end = s_dict[s[i+1]][1]
                continue
            right = s_dict[s[i]][1]
            end = max(end, right)

        return ans







# @lc code=end

