class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites, queries):
        # floyd
        graph = [[False for i in range(n)] for i in range(n)]
        for pair in prerequisites:
            graph[pair[0]][pair[1]] = True
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    graph[j][k] = (graph[j][i] and graph[i][k]) or graph[j][k]
        result = []
        for pair in queries:
            result.append(graph[pair[0]][pair[1]])
        return result

if __name__=='__main__':
    s = Solution()
    prerequisites = [[1,0],[2,1]]
    queries = [[0,2],[2,0]]
    n = 3
    print(s.checkIfPrerequisite(n,prerequisites,queries))