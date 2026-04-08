"""
LeetCode Problem: 155. Minstack
"""

#-----Solution----

class MinStack:
	
	def __init__(self):
		self.stack=[]
		self.minValues=[]
	def push(self, val: int) -> None:#存入主栈和最小值栈
		self.stack.append(val)
		if self.minValues==[]:
			self.minValues.append(val)
		else:
			self.minValues.append(min(self.minValues[-1],val))


	def pop(self) -> None:
		self.stack.pop()
		self.minValues.pop()
		#同时推出栈顶和栈顶对应最小值
		
	def top(self) -> int:
		return self.stack[-1]


	def getMin(self) -> int:
		if self.minValues!=[]:
			return self.minValues[-1]



