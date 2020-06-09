from LinkList.helper import TreeNode

class Solution:
    def treeToDoublyList(self, root: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        def dfs(tree_root):
            if tree_root:
                dfs(tree_root.left)
                if self.pre:
                    self.pre.right ,tree_root.left = tree_root,self.pre
                else:
                    self.head = tree_root
                self.pre = tree_root
                dfs(tree_root.right)
            else:
                return
        self.pre = None
        dfs(root)
        self.head.left,self.pre.right = self.pre,self.head
        return self.head
    