"""
LeetCode Problem: 3. lengthOfLongestSubstring
"""

class Solution:
    def solve(self,s):
        if s=="":
            return 0
        length =0
        start_flag = 0
        hashdict={}
        for i,x in enumerate(s):
            if x in hashdict and hashdict[x] >= start_flag:
                start_flag=hashdict[x]+1#上一个重复元素的下一个位置

            #字典记录位置
            hashdict[x]=i
            #子串长度是当前位置-startflag,即窗口长度
            windowslength=i-start_flag+1
            length=max(length,windowslength)
        return length


        


if __name__ == "__main__":
    s = Solution()
    

