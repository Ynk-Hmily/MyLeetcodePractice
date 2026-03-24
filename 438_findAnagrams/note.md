# 438. findAnagrams 🚀

## 题目描述 📄
![alt text](image.png)

---

## 思路 💡
1.暴力解：类似模板匹配一样去解

        def findAnagrams(s, p) :
            dictTemplate={}
            dictTarget={}
            slideLength =len(p)
            length=len(s)
            res=[]
            for x in p:
                dictTemplate[x]=dictTemplate.get(x,0)+1
            for i in range(0,length-slideLength+1):
                for t in range(slideLength):
                    dictTarget[s[i+t]]=dictTarget.get(s[i+t],0)+1
                if dictTarget==dictTemplate:
                    res.append(i)
                dictTarget.clear()
            return res
## 重新做窗口:x:耗时很大
## :white_check_mark:在上一次的窗口基础上-1,+1


---

## 算法复杂度 ⏱

| 类型 | 复杂度 |
|------|--------|
| 时间复杂度 | |
| 空间复杂度 | |

---

## 代码 💻

```python
# 写你的代码
```

---

## 测试用例 🧪


---

## 总结 📚

