#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1]:
            return True
        left = 0
        right = len(s)-1
        while(left<=right):
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                a = s[left+1:right+1]
                b = s[left:right]
                return a==a[::-1] or b==b[::-1]
        return True


# @lc code=end

