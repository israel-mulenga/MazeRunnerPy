# maze_model.py

class Cell:
    def __init__(self):
        self.walls = {'N': True, 'S': True, 'E': True, 'W': True}
        self.visited = False

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[Cell() for _ in range(width)] for _ in range(height)]

    def display(self):
        for row in range(self.height):
            # Print the north walls
            for col in range(self.width):
                if self.grid[row][col].walls['N']:
                    print("+---", end="")
                else:
                    print("+   ", end="")
            print("+")
            # Print the west walls and the cell itself
            for col in range(self.width):
                if self.grid[row][col].walls['W']:
                    print("|", end="")
                else:
                    print(" ", end="")
                print("   ", end="")
            print("|")
        # Print the south walls of the last row
        for col in range(self.width):
            print("+---", end="")
        print("+")

    def break_wall(self, x, y, direction):
        """Casse le mur de la cellule (x, y) dans la direction donnée et le mur opposé du voisin."""
        dx, dy = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}[direction]
        nx, ny = x + dx, y + dy
        # Vérifie que la cellule courante est dans la grille
        if not (0 <= x < self.height and 0 <= y < self.width):
            return
        # Casse le mur de la cellule courante
        self.grid[x][y].walls[direction] = False
        # Casse le mur opposé de la cellule voisine si elle existe
        opposites = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
        if 0 <= nx < self.height and 0 <= ny < self.width:
            self.grid[nx][ny].walls[opposites[direction]] = False

    def display_solution(self, path):
        """Affiche le labyrinthe avec le chemin de solution (marqué par '*')."""
        path_set = set(path)
        for row in range(self.height):
            # Ligne des murs nord
            for col in range(self.width):
                print("+---" if self.grid[row][col].walls['N'] else "+   ", end="")
            print("+")
            # Ligne des murs ou du chemin
            for col in range(self.width):
                print("|" if self.grid[row][col].walls['W'] else " ", end="")
                if (row, col) in path_set:
                    print(" * ", end="")
                else:
                    print("   ", end="")
            print("|")
        # Dernière ligne des murs sud
        for col in range(self.width):
            print("+---", end="")
        print("+")