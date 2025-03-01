import sys
from pprint import pprint
from collections import deque

from pathlib import Path

def search_start_end(title,maze):
    start_token = title[-2]
    end_token = title[-1]
    start = (0,0)
    end = (0,0)
    start_found = False
    end_found = False
    
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == start_token:
                start = i,j
                start_found = True
            elif maze[i][j] == end_token:
                end = i,j
                end_found = True
    
    if start_found and end_found:
        return start, end

    return None, None


def escape_maze(title,maze,start,end):
    maze_parameters = title[-5:]
    wall_slot = maze_parameters[0]

    rows = len(maze)
    cols = len(maze[0])

    #initialiser le tableau de gestion case visitée
    case_visitee = [[False] * cols for _ in range(rows)]
    # initialiser le dictionnaire de chemins
    precedemment = {}

    # - Définir les déplacements possibles depuis une cellule :
    # - (-1, 0) : déplacement vers le haut.
    # - (1, 0) : déplacement vers le bas.
    # - (0, -1) : déplacement vers la gauche.
    # - (0, 1) : déplacement vers la droite.

    directions = [(-1, 0),(1, 0),(0, -1),(0, 1)]

    fifo = deque([start])

    case_visitee[start[0]][start[1]] = True

    while fifo:

        courant = fifo.popleft()
        if courant == end:
            break
        
        for d in directions:
            prochaine_ligne = courant[0] + d[0]
            prochaine_colonne = courant[1] + d[1]
            prochaine_case = (prochaine_ligne,prochaine_colonne)

            if 0 <= prochaine_ligne < rows and 0 <= prochaine_colonne < cols:
                if not case_visitee[prochaine_ligne][prochaine_colonne] and maze[prochaine_ligne][prochaine_colonne] != wall_slot:
                    fifo.append(prochaine_case)
                    case_visitee[prochaine_ligne][prochaine_colonne] = True
                    precedemment[prochaine_case] = courant
        path = []

    case_ = end
    while case_ != start:
        path.append(case_)
        case_ = precedemment[case_]
    path.append(start)
    path.reverse()  # Inverser


    return path

    
def load_file(file_name):
    path_ = Path.cwd()
    fichier = path_ / file_name
    try:
        with open(fichier, "r", encoding="utf-8") as fichier:
            # On met le fichier en liste par ligne seulement si la ligne n'est pas vide
            first_line = fichier.readline().rstrip("\n")
            board = [list(ligne.rstrip("\n")) for ligne in fichier]
            #afficher(first_line,resultat)

        return first_line,board
    except FileNotFoundError:
        print(f"Erreur : Le fichier {fichier.name} n'existe pas.")
        return []
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return []
    
   
def args_are_valid(arguments):
    return len(arguments) == 1 and arguments[0].endswith(".map")


def board_is_valid(title ,maze):
    dimension_maze = title[:-5]
    x_index = dimension_maze.index("x")
    cols = int(dimension_maze[:x_index])
    rows = int(dimension_maze[x_index+1:])

    if not maze:
        return False

    if cols != len(maze):
        return False
    
    len_line_maze = all(len(line) == rows for line in maze)
    
    if not len_line_maze:
        return False
    
    return True


def display(first_line,maze,result):
    len_maze = len(maze)
    len_line_maze = len(maze[0])
    
    print(first_line)
    for i in range(len_maze):
        for j in range(len_line_maze):
            for r in result:
                if maze[i][j] != "1" and maze[i][j] != "2":
                    if i == r[0] and j == r[1]:
                        maze[i][j] = "o"
            
            print(maze[i][j],end="")
        print()


def error():
    print("error")


def main():
    arguments = sys.argv[1:]
    if args_are_valid(arguments):
        title, maze = load_file(arguments[0])
        if  board_is_valid(title,maze):
           start, end = search_start_end(title,maze)
           if start and end:
               result = escape_maze(title,maze,start,end)
               display(title,maze,result)
               
        else:
           error()
    else:
        error()


if __name__ == "__main__":
    main()