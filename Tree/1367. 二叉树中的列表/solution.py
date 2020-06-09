from Tree.helper import ListNode,TreeNode

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if head is None:
            return True
        if root is None:
            return False
        if self.dfs(head,root):
            return True
        return self.isSubPath(head,root.left) or self.isSubPath(head,root.right)

    def dfs(self,head: ListNode, root: TreeNode)->bool:
        if head is None:
            return True
        if root is None:
            return False
        if root.val !=head.val:
            return False
        return self.dfs(head.next,root.left) or self.dfs(head.next,root.right)

if __name__ == '__main__':
    s = Solution()
    listnode1 = ListNode(1)
    listnode2 = ListNode(2)
    listnode3 = ListNode(3)
    listnode1.next = listnode2
    listnode2.next = listnode3

    treenode1 = TreeNode(1)
    treenode2 = TreeNode(4)
    treenode3 = TreeNode(2)
    treenode4 = TreeNode(3)
    treenode5 = TreeNode(5)
    treenode1.left = treenode2
    treenode1.right = treenode3
    treenode2.right = treenode5
    treenode3.left = treenode4

    print(s.isSubPath(listnode1,treenode1))