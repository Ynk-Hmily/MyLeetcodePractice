### 三数之和
# 我的低效解
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
思路是划分了正负边界，分别处理正负情况的去重，实际上还是O(n^3)
# 优化解,正解：（排序+左右双指针）