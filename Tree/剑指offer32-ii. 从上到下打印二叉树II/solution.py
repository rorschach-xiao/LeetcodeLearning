from Tree.helper import TreeNode

class Solution:
    def levelOrder(self, root):
        Q = []
        print_list = []
        if root is None:
            return print_list
        Q.append(root)
        while (len(Q) != 0):
            temp = []
            for i in range(len(Q)):
                cur = Q.pop(0)
                temp.append(cur.val)
                if cur.left:
                    Q.append(cur.left)
                if cur.right:
                    Q.append(cur.right)
            print_list.append(temp)

        return print_list