"""
LeetCode Problem: 26. removeDuplicates
"""

#-----Solution----

def removeDuplicates(self, nums:list[int]) -> int:
	setnumbers=set()
	k=0
	for i in range(len(nums)):
		if nums[i] not in setnumbers:
			setnumbers.add(nums[i])
			nums[k]=nums[i]
			k+=1
		else:
			continue
	return k

#------Test----
def test():
	
	pass
if __name__ == "__main__":
    s = test()
