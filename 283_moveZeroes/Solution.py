"""
LeetCode Problem: 283. moveZeroes
"""

#-----Solution----

def moveZeroes(nums) -> None:
	flag=0#计数标记
	for i in range(len(nums)):
		if nums[i]!=0:
			nums[flag]=nums[i]
			flag+=1#这里已经跳到第一个归零位置了，下面不用+1
	for n in range(flag,len(nums)):
		nums[n]=0
	print(nums)

#------Test----
def test():
	case=[[0,1,0,3,12],[0,0,1],[0,1,0,3,12]]
	for x in case:
		moveZeroes(x)
		

if __name__ == "__main__":
    s = test()
