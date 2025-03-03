import sys

from pathlib import Path


def find_pattern_in_board(board,to_find):
    board_height = len(board)
    board_width = len(board[0])
    to_find_height = len(to_find)
    to_find_width = len(to_find[0])

    # on sauvegarde la première valeur à trouver
    to_find_first_value = "".join(to_find[0]).strip()[0]

    # on regarde si la matrice à rechercher n'est pas plus grande que le tableau
    if to_find_height > board_height or to_find_width > board_width:
        return False
    
    # on recherche la première correspondance du pattern dans le tableau
    for i in range(board_height - to_find_height + 1):
        for j in range(board_width - to_find_width + 1):
                if board[i][j] == to_find_first_value:
                    result = pattern_is_in(board, to_find, i, j)
                    
                    if result:
                        display(board, to_find, i, j)
                        return True
    return False


def pattern_is_in(board, to_find, board_height_pos, board_width_pos):
    to_find_height = len(to_find)
    to_find_width = len(to_find[0])

    for i in range(to_find_height):
        for j in range(to_find_width):
            if to_find[i][j] != " ":
                if board[board_height_pos + i][board_width_pos + j] != to_find[i][j]:
                    return False
    return True


def load_file(file_name):
    path_cwd = Path.cwd()
    fichier = path_cwd / file_name
    try:
        with open(fichier, "r", encoding="utf-8") as fichier:
            # On met le fichier en liste par ligne seulement si la ligne n'est pas vide
            resultat = [list(ligne.rstrip("\n")) for ligne in fichier if ligne]
        return resultat
    except FileNotFoundError:
        print(f"Erreur : Le fichier {fichier.name} n'existe pas.")
        return []
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return []


def len_arguments_is_valid(arguments,lenght):
    return len(arguments) == lenght


def has_arguments_end_with(argument,suffix):
    return argument.endswith(suffix)
   

def has_error(arguments):
    arguments_lenght = 2
    suffix = "txt"
    if not len_arguments_is_valid(arguments,arguments_lenght):
        print(f"Le nombre d'agument doit être de {arguments_lenght}")
        return True
    for argument in arguments:
        if not has_arguments_end_with(argument,suffix):
            print(f"Le nom de fichier ne termine pas pas {suffix}")
            return True
    
    return False


def get_arguments():
    arguments = sys.argv[1:]
    return arguments


def board_is_not_ok(board):
    if not board:
        return True
    return False


def to_find_is_not_ok(to_find,borad):
    if not to_find:
        return True
    return False


def display(board =[], to_find=[], i=0 , j=0):
    print("Trouvé !")
    print(f"Coordonnées : {i},{j}")

    for k in range(len(board)):  
        for l in range(len(board[0])):  
            # on regarde
            if i <= k < i + len(to_find) and j <= l < j + len(to_find[0]):
                # gestion des vides
                if to_find[k - i][l - j] != " ":
                    print(to_find[k - i][l - j], end="") 
                else:
                    print("-", end="")
            else:
                print("-", end="")
        print()  


def find_pattern():
    arguments = get_arguments()

    if has_error(arguments):
        return
    
    board = load_file(arguments[0])
    to_find = load_file(arguments[1])

    if board_is_not_ok(board) or to_find_is_not_ok(board,to_find):
        return

    if not  find_pattern_in_board(board,to_find):
         print("Introuvable")
    

find_pattern()