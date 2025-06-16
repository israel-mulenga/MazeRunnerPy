from collections import deque

def bfs_solve(maze, start, end):
    """
    Résout le labyrinthe avec BFS.
    maze: instance de Maze
    start: tuple (x, y) de départ
    end: tuple (x, y) d'arrivée
    Retourne le chemin sous forme de liste de tuples [(x1, y1), (x2, y2), ...]
    """
    queue = deque()
    queue.append((start, [start]))
    visited = set()
    visited.add(start)

    directions = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}

    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            return path
        for dir, (dx, dy) in directions.items():
            if not maze.grid[x][y].walls[dir]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < maze.height and 0 <= ny < maze.width and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), path + [(nx, ny)]))
    return None  # Aucun chemin trouvé