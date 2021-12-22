#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_dict = {}
        for item in t:
            if item not in char_dict.keys():
                char_dict[item]=1
            else:
                char_dict[item]+=1
        left = 0
        cnt = 0
        minlen = len(s)+1
        min_left = 0
        for right in range(0,len(s)):
            if s[right] in char_dict.keys():
                if char_dict[s[right]]>0:
                    cnt+=1
                char_dict[s[right]]-=1

                while(cnt==len(t)):
                    if (right-left+1)<minlen:
                        minlen=right-left+1
                        min_left=left
                    if s[left] in char_dict.keys():
                        char_dict[s[left]]+=1
                        if char_dict[s[left]]>0:                           
                            cnt-=1
                    left+=1
        return "" if minlen>len(s) else s[min_left:min_left+minlen]


# @lc code=end

if __name__=="__main__":
    sl = Solution()
    s = "ab"
    t = "a"
    sl.minWindow(s, t)