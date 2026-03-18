# Two Sums
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
数据集：nums = [2,7,11,15], target = 9
        nums = [3,2,4], target = 6
        nums = [3,3], target = 6
# HashTable
## 就是python的字典 dict
### 1、统计出现次数
    nums=[1,2,2,3,3,4,4,4]
    count={}
    for n in nums:
        count[n]=count.get(n,0)+1 
        #count.get(n,default) --获取key为n的value，若不存在返回default
        #这里利用第一次查询不存在就给count里存入一个0+1,实现记录出现一次，存在则更新一次实现了计数
    print("count:",count)
    #count:{1:1,2:2,3:3,4:3}
 
 ### 2、查找重复
 set()函数：创建一个无序不重复元素集合
 >>>x = set('runoob')
>>> y = set('google')
>>> x, y
(set(['b', 'r', 'u', 'o', 'n']), set(['e', 'o', 'g', 'l']))   # 重复的被删除
>>> x & y         # 交集
set(['o'])
>>> x | y         # 并集
set(['b', 'e', 'g', 'l', 'o', 'n', 'r', 'u'])
>>> x - y         # 差集
set(['r', 'b', 'u', 'n'])
>>>
