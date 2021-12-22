#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pos1 = m-1
        pos2 = n-1
        pos = m+n-1
        while(pos1>=0 and pos2>=0):
            if nums1[pos1]>nums2[pos2]:
                nums1[pos]=nums1[pos1]
                pos1-=1
                pos-=1
            else:
                nums1[pos]=nums2[pos2]
                pos2-=1
                pos-=1
        while(pos2>=0):
            nums1[pos]=nums2[pos2]
            pos-=1
            pos2-=1

# @lc code=end

