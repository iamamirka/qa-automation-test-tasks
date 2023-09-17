from collections import deque

class BreadthFirstSearch:

    def search_for_shortest_distance(self, total_matrix: ([], (int, int), (int, int))):
        matrix = total_matrix[0]
        start = total_matrix[1]
        target = total_matrix[2]
        rows_count = len(matrix)
        columns_count = len(matrix[0])
        #Possible movements: Down, Up, Right, Left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[False for _ in range(columns_count)] for _ in range(rows_count)]
        queue = deque([(start, [])])
        visited[start[0]][start[1]] = True

        while queue:
            (x, y), path = queue.popleft()
            if (x, y) == target:
                return path
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if (0 <= new_x < rows_count 
                    and 0 <= new_y < columns_count 
                    and not visited[new_x][new_y] 
                    and matrix[new_x][new_y] != 1):
                    new_path = path + [(x, y)]
                    queue.append(((new_x, new_y), new_path))
                    visited[new_x][new_y] = True
        return []
    