

import sys
from pprint import pprint

from pathlib import Path

path_ = Path.cwd()
arguments = sys.argv[1:]


def find_great_square(board):

    len_board = len(board)
    len_line_board = len(board[0])
    
    # Création de la matrice dp de même dimension
    dp = [[0] * len_line_board for _ in range(len_board)]
    max_size = 0
    top_left = None

    for i in range(len_board):
        for j in range(len_line_board):
            if board[i][j] == ".":  # Case vide
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                if dp[i][j] > max_size:
                    max_size = dp[i][j]
                    top_left = (i - max_size + 1, j - max_size + 1)
            else:
                dp[i][j] = 0

    if top_left is None:
        return None, None, 0
    else:
        return top_left[0], top_left[1], max_size

def load_file(file_name):
    fichier = path_ / file_name
    try:
        with open(fichier, "r", encoding="utf-8") as fichier:
            # On met le fichier en liste par ligne seulement si la ligne n'est pas vide
            first_line = fichier.readline().rstrip("\n")
            resultat = [list(ligne.rstrip("\n")) for ligne in fichier if ligne]
            #afficher(first_line,resultat)

        return first_line,resultat
    except FileNotFoundError:
        print(f"Erreur : Le fichier {fichier.name} n'existe pas.")
        return []
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return []
    
   
def verification_arguments(arguments):
    ok = False
    if len(arguments) == 1:
        if arguments[0].endswith("txt"):
            ok = True
    return ok


def afficher(first_line,result,square):
    len_result = len(result)
    len_line_result = len(result[0])
    
    x, y, square_size = square

    print(x, y , square_size)

    print(first_line)
    for i in range(len_result):
        for j in range(len_line_result):
            if x <= i < x + square_size and y <= j < y + square_size:
                print("o",end="")
            else: 
                print(result[i][j],end="")
        print()


def erreur():
    print("error")


def main():
    if verification_arguments(arguments):
        title, board = load_file(arguments[0])
        result = find_great_square(board)
        afficher(title,board,result)
    else:
        erreur()


if __name__ == "__main__":
    main()