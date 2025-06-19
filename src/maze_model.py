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
            # Ligne 1 : murs Nord
            top = ""
            middle = ""
            for col in range(self.width):
                # Coin + mur nord
                top += "+" + ("---" if self.grid[row][col].walls['N'] else "   ")
                # Mur ouest + espace cellule
                middle += ("|" if self.grid[row][col].walls['W'] else " ") + "   "
            top += "+"  # Dernier coin
            middle += "|"  # Bord droit de la ligne
            print(top)
            print(middle)
        
        # Ligne finale : murs Sud du dernier rang
        bottom = ""
        for col in range(self.width):
            bottom += "+---"
        bottom += "+"
        print(bottom)


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

    def display_solution(self, path, char='*', start_char='S', end_char='E'):
        """Affiche le labyrinthe avec le chemin (personnalisé) dans une seule boucle par ligne."""
        path_set = set(path)
        start_pos = path[0]
        end_pos = path[-1]

        for row in range(self.height):
            top = ""
            middle = ""
            for col in range(self.width):
                cell = self.grid[row][col]

                # Haut du bloc (mur nord)
                top += "+---" if cell.walls['N'] else "+   "

                # Mur ouest
                middle += "|" if cell.walls['W'] else " "

                # Contenu de la cellule
                pos = (row, col)
                if pos == start_pos:
                    middle += f" {start_char} "
                elif pos == end_pos:
                    middle += f" {end_char} "
                elif pos in path_set:
                    middle += f" {char} "
                else:
                    middle += "   "

            # Fermeture du top et du middle
            top += "+"
            middle += "|" if self.grid[row][-1].walls['E'] else " "
            print(top)
            print(middle)

        # Dernière ligne (mur sud)
        print("".join("+---" if self.grid[-1][col].walls['S'] else "+   " for col in range(self.width)) + "+")
