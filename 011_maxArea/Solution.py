"""
LeetCode Problem: 11. maxArea
"""

#-----Solution----

def maxArea(self, height: list[int]) -> int:
	maxOne=0
	for i in range(len(height)-1):
		for j in range(i+1,len(height)):
			area=(j-i)*min(height[i],height[j])
			maxOne=max(maxOne,area)
	return maxOne

def maxAreaNew(self, height: list[int]) -> int:
	maxarea=0
	left=len(height)-1#left表示的是末尾下标，要-1
	# for right in range(0,left): ##python for循环不会动态改变终点
	# 	candidateArea=min(height[right],height[left])*(left-right)
	# 	if height[right]<height[left]:
	# 		maxarea=max(maxarea,candidateArea)
	# 		continue
	# 	else:
	# 		maxarea=max(maxarea,candidateArea)
	# 		left-=1
	# 		continue
	right=0
	while right<left:
		candidateArea=min(height[right],height[left])*(left-right)
		maxarea=max(maxarea,candidateArea)
		if height[right]<height[left]:
			
			right+=1
		else:
			left-=1
	return maxarea


#------Test----
def test():
	pass


if __name__ == "__main__":
    s = test()
