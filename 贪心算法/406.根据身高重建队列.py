#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#

# @lc code=start
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: x[1])
        people.sort(key=lambda x: x[0], reverse=True)
        queue = []
        queue.append(people[0])
        for i in range(1, len(people)):
            if people[i][1]<len(queue):
                queue.insert(people[i][1], people[i])
            else:
                queue.append(people[i])
        return queue






# @lc code=end

