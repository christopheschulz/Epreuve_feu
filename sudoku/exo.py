import sys

from pprint import pprint
from pathlib import Path

path_ = Path.cwd()


def sudoku_resolve(sudoku):
    len_sudoku = 9
    len_line_sudoku = 9
    line_point = 0
    point_coordinate = 0
    sudoku_horizontal = []

    # premier passage horizontal, on regarde si 1 trou.
    for i in range(len_sudoku):
        line_point = 0
        for j in range(len_line_sudoku):
            if sudoku[i][j] == ".":
                line_point += 1
                point_coordinate = j
        if line_point == 1:
            number = find_number(sudoku[i])
            print(f"{number} est la valeure manquante de la ligne {i+1} à la position {point_coordinate+1}")
            sudoku[i][point_coordinate] = number

    return sudoku
    

def find_number(line_sudoku):
    sum_line_sudoku = 45

    int_line_sudoku = [int(i) for i in line_sudoku if i != "."]
    
    return sum_line_sudoku - sum(int_line_sudoku)


def load_file(file_name):
    fichier = path_ / file_name
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

   
def verification_arguments(arguments):
    ok = False
    if len(arguments) == 1:
        if arguments[0].endswith("txt"):
            ok = True
    return ok


def afficher(result):
    len_sudoku = 9
    len_line_sudoku = 9

    for i in range(len_sudoku):
        for j in range(len_line_sudoku):
            print(result[i][j],end="")
        print()

    
    pass


def erreur():
    print("error")


def main():
    arguments = sys.argv[1:]
    if verification_arguments(arguments):
        sudoku = load_file(arguments[0])
        result = sudoku_resolve(sudoku)
        afficher(result)
    else:
        erreur()


if __name__ == "__main__":
    main()