class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols + 1)] for _ in range(rows + 1)]
        count = 0

        def dfs(r, c):
            if visited[r][c] or r == rows or c == cols or r == -1 or c == - 1 or int(grid[r][c]) == 0:
                return
            
            visited[r][c] = True
            if not visited[r + 1][c]:
                dfs(r + 1, c)
            if not visited[r - 1][c]:
                dfs(r - 1, c)
            if not visited[r][c + 1]:
                dfs(r, c + 1)
            if not visited[r][c - 1]:
                dfs(r, c - 1)

        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and int(grid[i][j]) == 1:
                    dfs(i, j)
                    count += 1
                    
        return count
        