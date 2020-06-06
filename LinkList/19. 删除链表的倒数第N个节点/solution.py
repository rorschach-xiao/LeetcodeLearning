from LinkList.helper import ListNode

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast_ptr = head
        slow_ptr = head
        for i in range(n):
            fast_ptr = fast_ptr.next
        if fast_ptr is None:
            return head.next
        while(fast_ptr.next):
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next
        slow_ptr.next = slow_ptr.next.next
        return head

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    s = Solution()
    cur = s.removeNthFromEnd(n1,1)
    while(cur):
        print(cur.val)
        cur = cur.next


