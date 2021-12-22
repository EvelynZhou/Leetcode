#
# @lc app=leetcode.cn id=524 lang=python3
#
# [524] 通过删除字母匹配到字典里最长单词
#

# @lc code=start
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort()
        dictionary.sort(key=lambda x: len(x), reverse=True)
        for word in dictionary:
            l_word = 0
            l_str = 0
            while(l_str<len(s) and l_word<len(word)):
                if s[l_str]==word[l_word]:
                    l_str+=1
                    l_word+=1
                else:
                    l_str+=1
            if l_word==len(word):
                return word

        return ""

# @lc code=end

