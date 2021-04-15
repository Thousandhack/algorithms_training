"""
从尾到头打印链表
**题目：**输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

**思路：**将链表中的值记录到list之中，然后进行翻转list。

"""


class ListNode:
    """
    一个简单的链表
    """

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def ListFromTailToHead(self, listNode):
        Node_list = []  # 定义一个放链表元素的列表
        # 只要链表的下一个元素还存在就继续循环
        while listNode:
            Node_list.append(listNode.val)
            listNode = listNode.next
        return Node_list[::-1]


if __name__ == '__main__':
    """
    先生存元素
    """
    A1 = ListNode(1)
    A2 = ListNode(2)
    A3 = ListNode(3)
    A4 = ListNode(4)
    A5 = ListNode(5)
    """
    将元素产生关系
    """
    A1.next = A2
    A2.next = A3
    A3.next = A4
    A4.next = A5

    solution = Solution()
    ans = solution.ListFromTailToHead(A1)
    print(ans)
