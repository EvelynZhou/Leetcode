#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points):
        if len(points)<=1:
            return len(points)
        points.sort(key=lambda x: x[1], reverse=False)
        left = points[0][1]
        ans = 0
        index = 0
        for i in range(1, len(points)):
            if points[i][0]>left:
                ans+=1
                left=points[i][1]
                index = i-1
        if index<len(points)-1:
            ans+=1
        return ans

if __name__=="__main__":
    sl = Solution()
    input = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
    sl.findMinArrowShots(input)

# @lc code=end

