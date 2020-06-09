from Tree.helper import TreeNode

class Solution:
    def verifyPostorder(self, postorder):
        def helper(nums):
            if len(nums)<=1: return True
            root = nums[-1]
            for i in range(len(nums)):
                if nums[i]>root:break
            for j in range(i,len(nums)):
                if nums[j]<root:return False
            return helper(nums[:i]) and helper(nums[i:-1])
        return helper(postorder)

if __name__=='__main__':
    s = Solution()
    post_order = [1,2,3,4,5,6]
    print(s.verifyPostorder(post_order))