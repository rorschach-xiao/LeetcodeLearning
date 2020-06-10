class Solution:
    def permutation(self, s: str):
        perm_list = []

        def perm_helper(s, start, end):
            if start == end:
                perm_list.append(s)
                return
            else:
                for i in range(start, end):
                    if self.IsSwap(s, start, i):
                        s = self.swap(s, i, start)
                        perm_helper(s, start + 1, end)
                        s = self.swap(s, i, start)

        perm_helper(s, 0, len(s))
        return perm_list

    def IsSwap(self, s, start, end):
        for i in range(start, end):
            if s[i] == s[end]: return False
        return True

    def swap(self, s, i, j):
        s = list(s)
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        s = ''.join(s)
        return s