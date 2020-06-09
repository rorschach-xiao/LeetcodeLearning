from Tree.helper import TreeNode

class Solution:
    def levelOrder(self, root):
        Q = []
        print_list = []
        if (root is None):
            return print_list
        Q.append(root)
        while(len(Q)!=0):
            cur = Q.pop(0)
            if (cur.left):
                Q.append(cur.left)
            if (cur.right):
                Q.append(cur.right)
            print_list.append(cur.val)
        return print_list

