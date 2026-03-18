"""
LeetCode Problem: 13. romanToInt
"""

class Solution:
    def solve(self):
        dict={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        sum=0
        slist=list(s)
        for i in range(len(slist)-1):
            if dict[slist[i]]<dict[slist[i+1]]:
                sum-=dict[slist[i]]
            else:
                sum+=dict[slist[i]]
        sum+=dict[slist[-1]]


if __name__ == "__main__":
    s = Solution()
