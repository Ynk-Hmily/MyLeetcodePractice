"""
LeetCode Problem: 438. findAnagrams
"""

#-----Solution----


def findAnagrams(s, p) :
		dictTemplate={}
		dictTarget={}
		slideLength =len(p)
		length=len(s)
		res=[]
		for x in p:
			dictTemplate[x]=dictTemplate.get(x,0)+1
		start=0
		end=start+slideLength#indice+1实际indice+1
		if end < length:
			return[]
		if end == length:
			if sorted(p)==sorted(s):
				return[0]
			else:
				return[]
		while end<length:#匹配组比模板大的
			if start==0:#firstCheck
				for i in range(start,end):
					dictTarget[s[i]]=dictTarget.get(s[i],0)+1
				if dictTarget==dictTemplate:
					res.append(start)
				#slide
			dictTarget[s[start]]=dictTarget.get(s[start])-1#头部删去
			if dictTarget.get(s[start],0)==0:
				del dictTarget[s[start]]
			dictTarget[s[end]]=dictTarget.get(s[end],0)+1#尾部后1加入
			start+=1
			end+=1
			if dictTarget==dictTemplate:
				res.append(start)
		return res





				



#------Test----
def test():
	s="cbaebabacd"
	p="abc"
	print(findAnagrams(s,p))

if __name__ == "__main__":
    s = test()
