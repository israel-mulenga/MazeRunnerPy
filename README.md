# MazeRunnerPy

## Présentation du projet

MazeRunnerPy est une application Python permettant de générer, afficher et résoudre des labyrinthes en console. Le projet met en œuvre différents algorithmes classiques de génération et de résolution de labyrinthes (DFS, BFS) et propose une visualisation ASCII simple et efficace.

## Membres et responsabilités

- **Mulenga Nsembe Israel** : Responsable du modèle de labyrinthe et du générateur
- **Carlos** : Responsable de la résolution par DFS
- **Dimerce Akilimali** : Responsable de la résolution par BFS
- **Dieudonné** : Responsable du contrôleur principal

## Répartition des tâches

- **Modélisation du labyrinthe** : création des classes et structures de données
- **Génération du labyrinthe** : implémentation de l’algorithme DFS récursif (backtracking)
- **Résolution DFS** : recherche en profondeur pour trouver un chemin
- **Résolution BFS** : recherche en largeur pour trouver le chemin le plus court
- **Contrôleur principal** : gestion du flux du programme, affichage, interaction utilisateur

## Installation

Aucune installation n’est nécessaire.  
Aucun fichier `requirements.txt` ni environnement virtuel n’est requis.  
Le projet fonctionne avec une installation standard de Python 3.

## Lancement

1. Clonez ou téléchargez le projet dans un dossier local.
2. Placez-vous dans le dossier du projet :
   ```bash
   cd MazeRunnerPy
   ```
3. Lancez le contrôleur principal :
   ```bash
   python3 src/game_controller.py
   ```
   ou
   ```bash
   python src/game_controller.py
   ```

## Structure du projet

```
MazeRunnerPy/
│
├── src/
│   └── maze_model.py
│   └── maze_generator.py
│   └── dfs_solver.py
│   └── bfs_solver.py
│   └── game_controller.py
├── README.md
└── .gitignore
```

## Exemple de rendu ASCII

```
+---+---+---+---+---+
| S         |       |
+---+---+   +---+   +
|       |       |   |
+   +---+   +   +   +
|           |   |   |
+   +   +---+---+   +
|   |   |           |
+   +---+   +---+   +
|           |   | E |
+---+---+---+---+---+
```

## Remarques

- Le projet est conçu pour être simple à utiliser et à modifier.
- N’hésitez pas à explorer le code pour ajouter d’autres algorithmes ou une interface graphique.

---

*Projet réalisé par Mulenga Nsembe Israel, Carlos, Dimerce Akilimali et Dieudonné.*
