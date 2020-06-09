from LinkList.helper import  Node

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        cur = head
        while(cur):
            temp = Node(cur.val,cur.next)
            cur.next = temp
            cur = temp.next
        cur = head
        while(cur):
            if cur.next:
                if cur.random :
                    cur.next.random = cur.random.next
                cur = cur.next.next
        new_head = head.next
        cur = new_head
        while(cur and cur.next):
            cur.next = cur.next.next
            cur = cur.next
        return new_head