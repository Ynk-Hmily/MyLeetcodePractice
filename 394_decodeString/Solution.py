"""
LeetCode Problem: 394. decodeString
"""

#-----Solution----

def decodeString(self, s: str) -> str:
	res=""#动态的res变量
	statusStack=[]#存放状态的栈
	num=0#存放数字的中转变量
	for char in s:
		if char.isdigit():
			num=num*10+int(char)
			continue
		if char=="[":#存入栈并且重置res和num
			statusStack.append([num,res])
			res=""
			num=0
			continue
		if char=="]":#取出栈顶并拼接res
			res=statusStack[-1][1]+res*statusStack[-1][0]#用先前k前的res+当前的res×最近的括号的倍数k
			statusStack.pop()
			continue
		
		res=res+char
	return res


		



