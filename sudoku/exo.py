import sys

from pprint import pprint
from pathlib import Path

path_ = Path.cwd()


def sudoku_resolve(sudoku):
    # on cherche une case vide
    case = find_empty_box(sudoku)
    
    # si plus de case vide alors c'est gagné
    if not case:
        return True  
    
    # coordonnées de la case vide
    line, col = case

    for num in range(1, 10):  
        if is_valid(sudoku, line, col, num):
            # notre fichier sudoku est une chaine de caractère d'où le str()
            sudoku[line][col] = str(num)  

            if sudoku_resolve(sudoku):  
                return True
            # on remet un point si c'est pas la solution
            sudoku[line][col] = "." 

    return False  


def find_empty_box(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == ".":
                return i, j 
    return None  


def is_valid(sudoku, line, col, num):
    # Vérifier la ligne
    # notre fichier sudoku est une chaine de caractère d'où le str()
    if str(num) in sudoku[line]:
        return False
    
    # Vérifier la colonne
    # notre fichier sudoku est une chaine de caractère d'où le str()
    if str(num) in [sudoku[i][col] for i in range(9)]:
        return False
    
    # Vérifier le carré 3x3
    start_line, start_col = (line // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            # notre fichier sudoku est une chaine de caractère d'où le str()
            if sudoku[start_line + i][start_col + j] == str(num):
                return False
    
    return True


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
   
    for i in range(9):
        for j in range(9):
            print(result[i][j],end="")
        print()


def erreur():
    print("error")


def main():
    arguments = sys.argv[1:]
    if verification_arguments(arguments):
        sudoku = load_file(arguments[0])
        result = sudoku_resolve(sudoku)
        if result:
            afficher(sudoku)  
    else:
        erreur()


if __name__ == "__main__":
    main()