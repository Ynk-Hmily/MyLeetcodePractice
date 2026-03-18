#----Solution---
def longestConsecutive(nums:list[int])->int:
        if nums==[]:
             return 0
        numset=set(nums)
        max1=1#比较容器
        for x in numset:
            maxlength=1#计数器  
            if x-1 in numset:
                continue 
            while x+1 in numset:
                    x+=1
                    maxlength+=1
            max1=max(max1,maxlength)
                   
        return max1   
                
                