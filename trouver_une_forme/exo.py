import sys

from pprint import pprint
from pathlib import Path

chemin = Path.cwd()


def trouver_une_forme(board,to_find):
    board_height = len(board)
    board_width = len(board[0])
    to_find_height = len(to_find)
    to_find_width = len(to_find[0])
    result = False

    # on sauvegarde la première valeur à trouver
    to_find_first_value = "".join(to_find[0]).strip()[0]
    print("first value",to_find_first_value)

    # on regarde si la matrice à rechercher n'est pas plus grande que le tableau
    if to_find_height > board_height or to_find_width > board_width:
        return False
    
    # on recherche la première correspondance du pattern dans le tableau
    for i in range(board_height - to_find_height + 1):
        for j in range(board_width - to_find_width + 1):
                    if board[i][j] == to_find_first_value:
                        result = find_pattern(board, to_find, i, j)
                        if result == True:
                            return True
    return result


def find_pattern(board, to_find, board_height_pos, board_width_pos):
    to_find_height = len(to_find)
    to_find_width = len(to_find[0])

    print(to_find_height,to_find_width)

    print('find patern',board_height_pos,board_width_pos)
    
    for i in range(to_find_height):
        for j in range(to_find_width):
            print("range",i,j,board[board_height_pos + i][board_width_pos + j],to_find[i][j])
            if to_find[i][j] != " ":
                if board[board_height_pos + i][board_width_pos + j] != to_find[i][j]:
                    return False
    return True



def charger_fichier(nom_fichier):
    fichier = chemin / nom_fichier
    try:
        with open(fichier, "r", encoding="utf-8") as fichier:
            resultat = [list(ligne.rstrip("\n")) for ligne in fichier]
        return resultat
    except FileNotFoundError:
        print(f"Erreur : Le fichier {fichier.name} n'existe pas.")
        return []
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return []

   
def verification_arguments(arguments):
    ok = False
    if len(arguments) == 2:
        if arguments[0].endswith("txt") and arguments[1].endswith("txt"):
            ok = True
    return ok


def afficher(chaine):
   pass


def erreur():
    print("error")


def main():
    arguments = sys.argv[1:]
    if verification_arguments(arguments):
        board = charger_fichier(arguments[0])
        to_find = charger_fichier(arguments[1])
        if board and to_find:
            resultat = trouver_une_forme(board,to_find)
            print("resultat",resultat)
        else:
            erreur()   
    else:
        erreur()


if __name__ == "__main__":
    main()