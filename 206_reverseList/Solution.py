class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(nums):#列表输出成链表
    dummy = ListNode(0)
    cur = dummy
    for n in nums:
        cur.next = ListNode(n)
        cur = cur.next
    return dummy.next


def to_list(head):#链表以列表展示
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur=head
        prev=None
        while cur:
            temp=cur.next#先存当前链路
            cur.next=prev#反转指针
            prev=cur#prev前进
            cur=temp#cur前进
        return prev#prev到表尾作表头，cur超出
    
nums = [1, 2, 3, 4, 5]

head = build_list(nums)
sol=Solution()#创建1个实例对象sol
res=sol.reverseList(head=head)

print(to_list(res))


