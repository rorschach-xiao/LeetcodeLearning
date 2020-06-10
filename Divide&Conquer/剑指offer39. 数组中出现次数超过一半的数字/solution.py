class Solution:
    def majorityElement(self, nums):
        votes = 0
        for num in nums:
            if votes==0:res = num
            votes += 1 if res==num else -1
        return res

if __name__ =='__main__':
    s = Solution()
    l = [1,2,2,2,4,2,1]
    print(s.majorityElement(l))
