from maze_model import Maze

def dfs_solver(maze: Maze, start=(0, 0), end=None):
    """
    Résout le labyrinthe en utilisant la recherche en profondeur (DFS).
    Retourne le chemin de start à end sous forme de liste de tuples (row, col).
    """
    if end is None:
        end = (maze.height - 1, maze.width - 1)
    stack = [(start, [start])]
    visited = set()

    while stack:
        (current, path) = stack.pop()
        if current == end:
            return path
        if current in visited:
            continue
        visited.add(current)
        row, col = current
        cell = maze.grid[row][col]
        # Pour chaque direction, si pas de mur, avancer
        for direction, (dr, dc) in {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}.items():
            if not cell.walls[direction]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < maze.height and 0 <= nc < maze.width:
                    if (nr, nc) not in visited:
                        stack.append(((nr, nc), path + [(nr, nc)]))
    return None  # Aucun chemin trouvé