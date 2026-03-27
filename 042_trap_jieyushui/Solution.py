"""
LeetCode Problem: 42. trap_jieyushui
"""

#-----Solution----

def trap(height: list[int]) -> int:
	res=0
	leftMax=0
	rightMax=0
	left=0
	right=len(height)-1
	while left<=right:
		
		if leftMax<rightMax:
			leftMax=max(leftMax,height[left])
			
			res+=leftMax-height[left]
			left+=1
			
		else: 
			rightMax=max(rightMax,height[right])
			
			res+=rightMax-height[right]
			right-=1
			
	return res





#------Test----
def test():
	case=[[0,1,0,2,1,0,1,3,2,1,2,1]]
	for x in case:
	    print(trap(x))

if __name__ == "__main__":
    s = test()
