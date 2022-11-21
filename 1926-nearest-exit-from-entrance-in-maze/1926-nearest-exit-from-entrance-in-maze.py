class Solution:
    def nearestExit(self, grid: List[List[str]], entrance: List[int]) -> int:
        q = deque()
        q.append((entrance[0], entrance[1], 0))
        seen = set()
        while q :
            i, j, d = q.popleft()
            if (i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1) and [i, j] != entrance  :
                return d
            for x, y in ((i-1, j), (i, j-1), (i+1, j), (i, j+1)) :
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) :
                    if (x, y) not in seen and grid[x][y] == "." :
                        seen.add((x, y))
                        q.append((x, y, d+1))
                        # print(q)
        return -1