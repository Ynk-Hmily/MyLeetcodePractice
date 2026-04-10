"""
LeetCode Problem: 739. dailyTemperatures
"""

#-----Solution----

def dailyTemperatures( temperatures: list[int]) -> list[int]:
	stackCandidates=[]#辅助栈，存[值，下标]
	res=[]
	for i in range(len(temperatures)):
		while stackCandidates and temperatures[i]>stackCandidates[-1][0]:
			#栈内有待定且后续遇到大于栈顶,连续做
			v,k=stackCandidates.pop()
			res[k]=i-k
		if i!=len(temperatures)-1 and temperatures[i]<temperatures[i+1]:
			res.append(1)
		else:#小于等于
			res.append(0)#暂存0
			stackCandidates.append([temperatures[i],i])#存入辅助


	return res



def test():
	case=[89,62,70,58,47,47,46,76,100,70]
	result=dailyTemperatures(case)
	print(result)


if __name__ == "__main__":
    test()

