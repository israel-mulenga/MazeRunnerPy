import random
from maze_model import Maze

def generate_maze(height, width):
    maze = Maze(width, height)

    def visit(x, y):
        maze.grid[x][y].visited = True
        directions = ['N', 'S', 'E', 'W']
        random.shuffle(directions)
        for direction in directions:
            dx, dy = {'N': -1, 'S': 1, 'E': 0, 'W': 0}[direction], {'N': 0, 'S': 0, 'E': 1, 'W': -1}[direction]
            nx, ny = x + dx, y + dy
            if 0 <= nx < height and 0 <= ny < width and not maze.grid[nx][ny].visited:
                maze.break_wall(x, y, direction)
                visit(nx, ny)

    visit(0, 0)
    # Optionnel : remettre tous les visited à False pour la résolution
    for row in maze.grid:
        for cell in row:
            cell.visited = False
    return maze

if __name__ == "__main__":
    width = 10  # Example width
    height = 10  # Example height
    generated_maze = generate_maze(width, height)
    generated_maze.display()  # Assuming display method is defined in Maze class