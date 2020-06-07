class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        # initial dp matrix
        dp = [[i+j if (j==0 or i==0) else 0 for i in range(len2+1)] for j in range(len1+1)]
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+1)
        return dp[len1][len2]

if __name__ == '__main__':
    s = Solution()
    word1 = 'apple'
    word2 = 'appreciate'
    print(s.minDistance(word1,word2))