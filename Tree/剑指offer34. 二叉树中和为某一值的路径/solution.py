from Tree.helper import TreeNode

class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        self.res = []
        self.path = []
        def dfs(root, target):
            if root is None:return 
            self.path.append(root.val)
            target-=root.val
            if target==0 and not root.left and not root.right:
                self.res.append(list(self.path))
            dfs(root.left,target)
            dfs(root.right,target)
            self.path.pop()
        dfs(root,sum)
        return self.res
