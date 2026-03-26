"""
LeetCode Problem: 42. trap_jieyushui
"""

#-----Solution----

def trap(height: list[int]) -> int:
	res=0
	for i in range(1,len(height)-1):
		left=i-1
		right=i+1
		if height[i]>height[left] or height[i]>=height[right]: 
			#跳过i:1\大于任意左右一边，2\等于右边就跳
			continue
		
		leftend=False
		rightend=False
		# if left<0:continue
		# if right>=len(height):break
		while not leftend:
			if left-1<0 or height[left]>height[left-1]:
				leftend=True
				break
			left-=1
		while not rightend:
			if right==len(height)-1 or height[right]>height[right+1]:
				rightend=True
				break
			right+=1
		#边界等于底边情况筛选：
		if height[left]==height[i] or height[right]==height[i]:
			continue
		#左右边界比较
		thresh=min(height[left],height[right])
		width=right-left-1
		area=thresh*width
		for n in range(left+1,right):
			if height[n]>=thresh:
				area-=thresh
			else:
				area-=height[n]
		res+=area
	return res
		






#------Test----
def test():
	case=[[4,2,0,3,2,5]]
	for x in case:
	    print(trap(x))

if __name__ == "__main__":
    s = test()
