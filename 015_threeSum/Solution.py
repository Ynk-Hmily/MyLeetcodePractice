"""
LeetCode Problem: 15. threeSum
"""

#-----Solution----

def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []
    noNegativeNumsIndice=[i for i,x in enumerate(nums) if x>=0]
    noNegativeNums=[x for i, x in enumerate(nums) if x>=0]
    if len(noNegativeNums)==len(nums):
        if(nums[0]+nums[1]+nums[2]==0):
            res.append([nums[0],nums[1],nums[2]])
            return res
        else:
            return res

    elif len(noNegativeNums)>=3 and noNegativeNums[0]+noNegativeNums[1]+noNegativeNums[2]==0:
        res.append([noNegativeNums[0],noNegativeNums[1],noNegativeNums[2]])
    elif len(noNegativeNums)==0:
        return res
#判断【0,0,0,0,1】这种情况
    zeroMark=noNegativeNumsIndice[0]
    dupStarts={}
    for i in range(0,zeroMark):#左起点
        if nums[i]==nums[i+1]:#起点重复(左半重复)
            if nums[i] in dupStarts:
                continue
            else:
                dupStarts[nums[i]]=i
                for m in range(zeroMark,len(nums)):
                    if nums[m]+2*nums[i]==0:
                        res.append([nums[i],nums[i],nums[m]])
                        break
                continue
        for j in range(i+1,zeroMark):#二号标记未过零分界
            if nums[j]==nums[j+1]:#二号标记重复
                continue
            else:
                for k in range(zeroMark,len(nums)):#三号标记必正
                    if k<len(nums)-1 and nums[k]==nums[k+1]:#三号标记重复,跳过
                        continue
                    else:
                        if nums[i]+nums[j]+nums[k]==0:
                            res.append([nums[i],nums[j],nums[k]])
                            break
        for j in range(zeroMark,len(nums)-1):#二号标记过零分界
            if nums[j]==nums[j+1]:#二号标记重复（右半重复）
                if nums[j] in dupStarts:
                    continue
                else:
                    dupStarts[nums[j]]=j
                    for n in range(0,zeroMark):#这里不能到zeromark,ex:[-1,0,0,1],三个0情况放前面
                        if nums[n]+nums[j]+nums[j+1]==0:
                            res.append([nums[n],nums[j],nums[j+1]])
                            break
                    continue
            else:
                for k in range(j+1,len(nums)):
                    if k<len(nums)-1 and nums[k]==nums[k+1]:#三号标记重复,跳过
                        continue
                    else:
                        if nums[i]+nums[j]+nums[k]==0:
                            res.append([nums[i],nums[j],nums[k]])
                            break
    return res

def threeSum2( nums: list[int]) -> list[list[int]]:
    nums.sort()
    res=[]
    for i in range(0,len(nums)-2):#
        if i>0 and nums[i]==nums[i-1]:#起点重复
            continue
        right=len(nums)-1
        left=i+1    
        while left<right:
            if nums[i]+nums[right]+nums[left]==0:
                res.append([nums[i],nums[right],nums[left]])
                left+=1
                right-=1
                while left<right and nums[left]==nums[left-1]:#跳过重复
                    left+=1
                while left<right and nums[right]==nums[right+1]:#跳过重复
                    right-=1
            elif nums[i]+nums[right]+nums[left]>0:
                right-=1
            elif nums[i]+nums[right]+nums[left]<0:
                left+=1
           
            continue
    return res

#------Test----
def test():
	result=[]
	case=[[-1,0,1,2,-1,-4],[0,0,0,0],[2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]]
	for x in case:
		result=threeSum2(nums=x)
		print(result)

	

if __name__ == "__main__":
    test()
