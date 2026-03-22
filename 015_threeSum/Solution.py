"""
LeetCode Problem: 15. threeSum
"""

#-----Solution----

def Solution(nums: list[int]):
	res=[]
	if len(nums)<3:
		return []
	if len(nums)==3:
		if (nums[0]+nums[1]+nums[2]==0):
			return[nums]
		else :return[]
	nums.sort()
	print(nums)
	noNegativeNumsIndice= [i for i,x in enumerate(nums) if x >= 0]
	noNegativeNums=[x for i,x in enumerate(nums)if x >=0]
	print(noNegativeNums)
	if len(noNegativeNums)==len(nums):
		if noNegativeNums[0]+noNegativeNums[1]+noNegativeNums[2]==0:
			return[[0,0,0]]
		else:
			return[]
	zeroMark=noNegativeNumsIndice[0]
	#return[zeroMark,noNegativeNums,nums]
	dupStarts={}
	for i in range(0,zeroMark):#起点标记在非负部
		if nums[i]==nums[i+1]:#重复起点
			if nums[i] in dupStarts:
				continue
			else:
				dupStarts[nums[i]]=i
				for m in range(zeroMark,len(nums)):
					#print("d")
					if nums[m]+nums[i]+nums[i+1]==0:
						res.append([nums[m],nums[i],nums[i]])
						#print(res)
						continue
					
				continue
			
		for j in range(i+1,len(nums)-1):
			#print("j",j)#二次标记在起点左to倒数第二位
			if j >= zeroMark:#二号标记走至零分界
				if nums[j]==nums[j+1]:
					if nums[j] in dupStarts:
						#print("jump")
						continue
					else:
						dupStarts[nums[j]]=j
						if nums[j]*2+nums[i]==0:
							res.append([nums[j],nums[j],nums[i]])
							continue
						else:
							#print('jmp')
							continue
				for k in range(j+1,len(nums)):#三号标记从二号标记开始to末尾
					if k<len(nums)-1 and nums[k]==nums[k+1]:
						if nums[k] in dupStarts:
							continue
						else:
							dupStarts[nums[k]]=k
							if nums[k]+nums[k]+nums[i]==0:
								res.append([nums[k],nums[k],nums[i]])
								continue
							else:continue
					if nums[k]+nums[j]+nums[i]==0:
						res.append([nums[k],nums[j],nums[i]])

			else:#二号标记没过零线
				if nums[j]==nums[j+1]:
					continue
				for k in range(zeroMark,len(nums)):#三号标记从零线to末尾
					if k<len(nums)-1 and nums[k]==nums[k+1]:
						continue
					if(nums[k]+nums[j]+nums[i]==0):
						res.append([nums[k],nums[j],nums])
						
	return(res)

#------Test----
def test():
	result=[]
	case=[[-1,0,1,2,-1,-4],[0,0,0,0],[2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]]
	for x in case:
		result=Solution(nums=x)
		print(result,"/n----")

	

if __name__ == "__main__":
    test()
