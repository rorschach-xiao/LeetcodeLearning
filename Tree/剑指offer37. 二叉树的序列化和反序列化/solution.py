from Tree.helper import TreeNode

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        Q = []
        if not root:
            return str([])
        Q.append(root)
        seq = []
        while (len(Q) != 0):
            cur = Q.pop(0)
            if cur:
                seq.append(cur.val)
                Q.append(cur.left)
                Q.append(cur.right)
            else:
                seq.append(None)
        seq_str = '['
        for i in seq:
            if i is None:
                seq_str += 'null,'
            else:
                seq_str += str(i) + ','
        return seq_str

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if data == '[]':
            return None
        seq = data[1:-1].split(',')
        root = TreeNode(int(seq[0]))
        Q = []
        Q.append(root)
        index = 1
        while (len(Q) != 0):
            cur = Q.pop(0)
            if seq[index] != 'null':
                cur.left = TreeNode(int(seq[index]))
                Q.append(cur.left)
            index += 1
            if seq[index] != 'null':
                cur.right = TreeNode(int(seq[index]))
                Q.append(cur.right)
            index += 1
        return root
