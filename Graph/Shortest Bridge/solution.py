class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:  
        directions = [(0,1), (0,-1), (1,0), (-1,0)] 
        m = len(grid)
        n = len(grid[0])
        start = None
        # find first land node
        for i in range(m):
            if start is not None:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                    break
                    
        queue = [start]
        first_land = [start]
        
        visited = dict()
        visited[start] = True    
        # find all first land node
        while first_land:
            x, y = first_land.pop(0)
            for dir_x, dir_y in directions:
                neighbor_x = x + dir_x
                neighbor_y = y + dir_y
                if neighbor_x in range(m) and neighbor_y in range(n):       
                    neighbor = (neighbor_x, neighbor_y)
                    if grid[neighbor_x][neighbor_y] == 1 and neighbor not in visited:   
                        first_land.append(neighbor)
                        queue.append(neighbor)
                        visited[neighbor] = True
        # bfs from first land node to find second island
        cost = 0
        q_size = 0
        while queue:
            q_size = len(queue)
            for i in range(q_size):
                (x, y) = queue.pop(0)
                for dir_x, dir_y in directions:
                    neighbor_x = x + dir_x
                    neighbor_y = y + dir_y
                    if neighbor_x in range(m) and neighbor_y in range(n):     
                        neighbor = (neighbor_x, neighbor_y)
                        if neighbor not in visited:
                            if grid[neighbor_x][neighbor_y] == 1:
                                return cost
                            else:
                                queue.append(neighbor)
                                visited[neighbor] = True
            cost += 1
        return cost