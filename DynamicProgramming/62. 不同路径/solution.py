class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 if (j!=0 and i!=0) else 1 for j in range(n)] for i in range(m)]
        for i in range(1,m):
            for j  in range(1,n):
                    dp[i][j] = dp[i][j-1]+dp[i-1][j]
        return dp[m-1][n-1]

if __name__=='__main__':
    m=7
    n=3
    s=Solution()
    print(s.uniquePaths(m,n))
