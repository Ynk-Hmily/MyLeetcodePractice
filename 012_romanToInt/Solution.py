"""
LeetCode Problem: 12. romanToInt
"""

#-----Solution-----
class Solution:
    def solution(self,num):
        dictRoman={
             1:'I',
             5:'V',
             10:'X',
             50:'L',
             100:'C',
             500:'D',
             1000:'M'
        }
        count=0
        while num!=0:
            num//=10 
            count+=1
        
        #10*(count-1)


#------Test-----
    def test():
	    case=[]


if __name__ == "__main__":
    s = Solution()
