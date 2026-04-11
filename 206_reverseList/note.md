# 206. reverseList 🚀

## 题目描述 📄

反转链表

---

## 思路 💡
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        prev=None
        while cur:
            temp=cur.next#先存当前链路
            cur.next=prev#反转指针
            prev=cur#prev前进
            cur=temp#cur前进
        return prev#prev到表尾作表头，cur超出

```

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

