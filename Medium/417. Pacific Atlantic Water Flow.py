class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if len(heights) == 0:
            return []
        row,col = len(heights),len(heights[0])
        p_q = []
        p_visited = [[False]*col for _ in range(row)]
        a_q = []
        a_visited = [[False]*col for _ in range(row)]
        print()
        for i in range(len(heights[0])):
            p_q.append((0,i))
            p_visited[0][i] = True
            a_q.append((row-1,i))
            a_visited[row-1][i] = True
        for j in range(len(heights)):
            p_q.append((j,0))
            p_visited[j][0] = True
            a_q.append((j,col-1))
            a_visited[j][col-1] = True
        def DFS(q,visited):
            while q:
                row,col = q.pop(0)
                for i,j in [(0,1),(1,0),(0,-1),(-1,0)]:
                    y = row + i
                    x = col + j
                    if 0 <= y < len(visited) and 0 <= x < len(visited[0]):
                        if heights[row][col] <= heights[y][x] and not visited[y][x]:
                            visited[y][x] = True
                            q.append((y,x))
            
        DFS(p_q,p_visited)
        DFS(a_q,a_visited)

        ans = []
        for i in range(row):
            for j in range(col):
                if p_visited[i][j] and a_visited[i][j]:
                    ans.append([i,j])
        return ans