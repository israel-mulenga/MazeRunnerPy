from maze_generator import generate_maze
from dfs_solver import dfs_solver
from bfs_solver_visualizer import bfs_solve

maze = generate_maze(15, 19)  # Génère un labyrinthe 10x10

print("Labyrinthe :")
maze.display()

# Résolution avec DFS du coin supérieur gauche au coin inférieur droit
# path = dfs_solver(maze, start=(0, 0), end=(9, 9))
# maze.display_solution(path, char='*')

path = bfs_solve(maze, start=(0, 0), end=(9, 9))
print("\nSolution trouvée :")
maze.display_solution(path, char='o')