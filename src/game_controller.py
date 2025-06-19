import pickle
from maze_model import Maze
from maze_generator import generate_maze
from dfs_solver import dfs_solver
from bfs_solver_visualizer import bfs_solve

def afficher_menu():
    print("\n--- Maze Runner ---")
    print("1. Générer un nouveau labyrinthe")
    print("2. Charger un labyrinthe avec sa solution")
    print("3. Quitter")

def choisir_algorithme():
    print("\nChoisissez l'algorithme de résolution :")
    print("1. DFS (Depth-First Search)")
    print("2. BFS (Breadth-First Search)")
    while True:
        choix = input("Votre choix : ")
        if choix in ("1", "2"):
            return choix
        print("Choix invalide. Veuillez entrer 1 ou 2.")

def enregistrer_labyrinthe(maze, solution):
    nom = input("Nom du fichier à enregistrer : ")
    try:
        with open(nom, "wb") as f:
            pickle.dump({'maze': maze, 'solution': solution}, f)
        print("Labyrinthe et solution enregistrés.")
    except Exception as e:
        print(f"Erreur lors de l'enregistrement : {e}")

def charger_labyrinthe():
    nom = input("Nom du fichier à charger : ")
    try:
        with open(nom, "rb") as f:
            data = pickle.load(f)
        print("Labyrinthe chargé.")
        return data['maze'], data['solution']
    except Exception as e:
        print(f"Erreur lors du chargement : {e}")
        return None, None

def demander_coordonnees(message, largeur, hauteur):
    while True:
        try:
            x = int(input(f"{message} x (0 à {largeur-1}) : "))
            y = int(input(f"{message} y (0 à {hauteur-1}) : "))
            if 0 <= x < largeur and 0 <= y < hauteur:
                return y, x  # (ligne, colonne)
            else:
                print("Coordonnées hors limites.")
        except ValueError:
            print("Veuillez entrer des entiers valides.")

def main():
    while True:
        afficher_menu()
        choix = input("Votre choix : ")
        if choix == "1":
            try:
                largeur = int(input("Largeur du labyrinthe : "))
                hauteur = int(input("Hauteur du labyrinthe : "))
                maze = generate_maze(hauteur, largeur)
                maze.display()
                start = demander_coordonnees("Départ", largeur, hauteur)
                end = demander_coordonnees("Arrivée", largeur, hauteur)
                algo = choisir_algorithme()
                if algo == "1":
                    solution = dfs_solver(maze, start, end)
                else:
                    solution = bfs_solve(maze, start, end)
                print("\nLabyrinthe résolu :")
                if solution:
                    maze.display_solution(solution, "o")
                else:
                    print("Aucune solution trouvée.")
                save = input("Enregistrer ce labyrinthe et sa solution ? (o/n) : ")
                if save.lower() == "o":
                    enregistrer_labyrinthe(maze, solution)
            except Exception as e:
                print(f"Erreur : {e}")
        elif choix == "2":
            maze, solution = charger_labyrinthe()
            if maze is not None and solution is not None:
                print("\nLabyrinthe chargé avec sa solution :")
                if solution:
                    maze.display_solution(solution)
                else:
                    maze.display()
        elif choix == "3":
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()