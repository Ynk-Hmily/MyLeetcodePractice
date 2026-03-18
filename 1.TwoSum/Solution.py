#---solution---
def twoSums(nums:list[int],target:int):
    #n重遍历
    #hash表，遍历一遍，记录下每个元素的位置，当target-当前元素在hash中，返回下标
    hash={}
    for i,num in enumerate(nums):
        if target-num in hash:
            return [i,hash[target-num]]
        hash[num]=i
def test():
    cases=[([2,7,11,15],9),([3,2,4],6),([3,3],6)]
    for num,tar in cases:
        result=twoSums(nums=num,target=tar)
        print("input:",num,tar)
        print("res:",result)
        print("----------")

if __name__=="__main__":
    test()



