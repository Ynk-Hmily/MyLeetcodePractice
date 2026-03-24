#------Solution---
from collection import defaultdict
def groupAnagrams(strs:list[str])->list[list[str]]:
    statis=defaultdict(list)
    for str in strs:
        sortedStr_list=sorted(str)#自动排序函数,返回列表，下一步需要转
        sortedStr="".join(sortedStr_list)#join 拼接函数
        statis[sortedStr].append(str)
    return list(statis.value())
