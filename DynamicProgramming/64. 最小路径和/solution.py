class Solution:
    def minPathSum(self, grid):
        height = len(grid)
        width = len(grid[0])
        dp = [[0 for j in range(width)] for i in range(height)]
        for i in range(height):
            for j in range(width):
                if i-1<0 and j-1>=0:
                    dp[i][j] = dp[i][j-1]+grid[i][j]
                elif i-1>=0 and j-1<0:
                    dp[i][j] = dp[i-1][j]+grid[i][j]
                elif i-1>=0 and j-1>=0:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]
                else:
                    dp[i][j] = grid[i][j]
        return dp[height-1][width-1]

if __name__ == '__main__':
    grid = [[1,2,1],[3,4,1],[2,1,5]]
    s = Solution()
    print(s.minPathSum(grid))