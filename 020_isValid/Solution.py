"""
LeetCode Problem: 20. isValid
"""

#-----Solution----

def isValid(self, s: str) -> bool:
	#创建一个键值对字典：
	pairs={
		")":"(",
		"}":"{",
		"]":"["
	#反过来存储，用左半边做key
	}
	stack=[]
	for x in s:
		if x in pairs and len(stack)!=0 :
			#遇到右半边进行比较
			if stack[-1]==pairs[x] :#匹配
				stack.pop()#匹配则将最后一位弹出
			else:#不匹配
				return False
		else:#不遇到右半边则保持存进
			stack.append(x)
	if stack==[]:
		return True
	else:
		return False



#------Test----
def test():
	pass

if __name__ == "__main__":
    s = test()
