# 283. moveZeroes 🚀

## 题目描述 📄
### 移动0到列表末尾

---

## 思路 💡
:x:用i遍历，遇到0删除然后append:x:**列表变化，i变化，会漏解**
:white_check_mark:用一个标记位，判断仅在标记位进行

     flag =0
        for i in range(len(nums)):
            if nums[flag]!=0:
                flag+=1
            else:
                del nums[flag]
                nums.append(0)
13ms:问题在于del是O(n)操作，时间开销大，加上这样会动态变化数组长度，加大for in range 的时间开销

## 思路优化 💡
用替换元素修改元素代替删除操作
寻找非零元素
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

